from os import getenv
from flask import Flask, jsonify, request
from flasgger import Swagger

from app.controllers.signup import SignupController
from app.controllers.signin import SigninController
from app.controllers.get_locale_forecast import GetLocaleForecastController

from app.repositories.user import MongoDBUserRepository
from app.repositories.forecast import APIForecastRepository

from domain.usecases.signup_user import SignupUser
from domain.usecases.signin_user import SigninUser
from domain.usecases.get_locale_forecast import GetLocaleForecast

from app.config.middlewares import es_log, get_user_logs, auth

DB_URI = getenv('DB_URI')
DB_NAME = getenv('DB_NAME')

user_repository = MongoDBUserRepository(DB_URI, DB_NAME)
forecast_repository = APIForecastRepository()

signup_usecase = SignupUser(user_repository)
signin_usecase = SigninUser(user_repository)
get_locale_forecast_usecase = GetLocaleForecast(forecast_repository)

signup_controller = SignupController(signup_usecase)
signin_controller = SigninController(signin_usecase)
get_locale_forecast_controller = GetLocaleForecastController(get_locale_forecast_usecase)

app = Flask('TargetData API')
app.config['SWAGGER'] = {
    'title': 'TargetData API Docs',
    'uiversion': 3,
    'version': '1.0',
    'description': 'TargetData API endpoints usage'
}

docs = Swagger(app)

@es_log
@app.route('/auth/signup', methods=['POST'])
def signup_user():
    """Sign Up user
    ---
    parameters:
        - name: username
          in: body
          type: string
          required: true
          example: foo
        - name: password
          in: body
          type: string
          required: true
          example: bar
    responses:
      200:
        description: Confirmation of user registration
        schema:
            id: SignupResult
            type: object
            properties:
                status:
                    type: string
        example:
          status: ok
    """
    result = signup_controller.handle(request.json)

    return jsonify(result)

@es_log
@app.route('/auth/signin', methods=['POST'])
def signin_user():
    """Sign In user
    ---
    parameters:
        - name: username
          in: body
          type: string
          required: true
          example: foo
        - name: password
          in: body
          type: string
          required: true
          example: bar
    responses:
      200:
        description: a token representing the user session
        schema:
            id: SigninResult
            type: object
            properties:
                token:
                    type: string
        examples:
          token: jwt token
    """
    result = signin_controller.handle(request.json)

    return jsonify(result)

@es_log
@auth
@app.route('/forecast', methods=['POST'])
def get_forecast():
    """Get Forecast
    ---
    parameters:
        - name: locale_cep
          in: body
          type: string
          required: true
          example: 11021001
    definitions:
        ForecastData:
            type: object
            properties:
                date:
                    type: string
                weather:
                    type: string
                max:
                    type: string
                min:
                    type: string
                iuv:
                    type: string
    responses:
      200:
        description: Info of locale and its forecast
        schema:
            id: GetForecastResult
            type: object
            properties:
                forecast:
                    type: object
                    properties:
                        cep:
                            type: string
                        address:
                            type: string
                        complement:
                            type: string
                        neighborhood:
                            type: string
                        name:
                            type: string
                        uf:
                            type: string
                        ibge_code:
                            type: string
                        gia_code:
                            type: string
                        ddd_code:
                            type: string
                        siafi_code:
                            type: string
                locale:
                    type: object
                    properties:
                        locale_name:
                            type: string
                        locale_uf:
                            type: string
                        updated_at:
                            type: string
                        forecasts:
                            type: array
                            items:
                                $ref: '#/definitions/ForecastData'
    """
    result = get_locale_forecast_controller.handle(request.json)

    return jsonify(result)

@es_log
@auth
@app.route('/logs', methods=['GET'])
def get_logs():
    """Get Logs
    ---
    responses:
      200:
        description: Info of all user requests made to API
        schema:
            id: GetLogsResult
            type: array
            items:
                schema:
                    id: Log
                    properties:
                        timestamp:
                            type: string
                        url:
                            type: string
                        method:
                            type: string
                        user_token:
                            type: string
                        url_params:
                            type: object
                        request_body:
                            type: object
    """
    logs = get_user_logs(request.headers.get('authorization'))

    return jsonify({'logs': logs})

@es_log
@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'error': 'route not found'})

@es_log
@app.errorhandler(405)
def invalid_method(e):
    return jsonify({'error': 'invalid method'})

@es_log
@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'internal server error'})

if __name__ == '__main__':
    app.run(debug=True)