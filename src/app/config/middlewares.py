from os import getenv
from datetime import datetime
from flask import request, jsonify
from elasticsearch import Elasticsearch
from functools import wraps
from typing import Callable

es = Elasticsearch(
    hosts=[{'host': 'api-logs', 'scheme': 'http', 'port': 9200}]
)

def es_log(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args, **kwargs) -> Callable:
        doc = {
            'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M:%S.%f'),
            'url': request.url,
            'method': request.method,
            'user_token': request.headers.get('authorization'),
            'url_params': request.args.to_dict()
        }

        if request.content_type == 'application/json':
            doc['request_body'] = request.json

        es.index(index='requests', document=doc)

        return fn(*args, *kwargs)
    return wrapper

def get_user_logs(user_token: str) -> list[dict]:
    search_query = {
        'query': {
            'match': {
                'user_token': user_token
            } 
        }
    }

    result = es.search(index='requests', body=search_query)

    logs = [x['_source'] for x in result['hits']['hits']]

    return logs

def auth(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args, **kwargs) -> Callable:
        token = request.headers.get('authorization')

        if not token:
            return jsonify({'error': 'authorization token required'})

        return fn(*args, **kwargs)
    return wrapper