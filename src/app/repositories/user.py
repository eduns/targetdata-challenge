from werkzeug.security import check_password_hash, generate_password_hash

from pymongo import MongoClient

from domain.repositories.user import UserRepository

class MongoDBUserRepository(UserRepository):
    def __init__(self, db_uri: str, db_name: str) -> None:
        self.db = MongoClient(db_uri)[db_name]

    def get(self, criteria: dict) -> dict:
        result = self.db.users.find_one({
            'username': criteria.get('username')
        }, {'_id': 0})

        if result and check_password_hash(result.get('password_hash'), criteria.get('password')):
            return result

        return None

    def add(self, user_data: dict) -> None:
        self.db.users.insert_one({
            'username': user_data.get('username'),
            'password_hash': generate_password_hash(user_data.get('password'), method='sha256')
        })