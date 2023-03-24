from os import getenv
from flask import Flask, jsonify, request

from app.controllers.signup import SignupController
from app.controllers.signin import SigninController
from app.controllers.get_locale_forecast import GetLocaleForecastController

from app.repositories.user import MongoDBUserRepository
from app.repositories.forecast import APIForecastRepository

from domain.usecases.signup_user import SignupUser
from domain.usecases.signin_user import SigninUser
from domain.usecases.get_locale_forecast import GetLocaleForecast

DB_URI = getenv('DB_URI')
DB_NAME = getenv('DB_NAME')

app = Flask('TargetData API')

user_repository = MongoDBUserRepository(DB_URI, DB_NAME)
forecast_repository = APIForecastRepository()

signup_usecase = SignupUser(user_repository)
signin_usecase = SigninUser(user_repository)
get_locale_forecast_usecase = GetLocaleForecast(forecast_repository)

signup_controller = SignupController(signup_usecase)
signin_controller = SigninController(signin_usecase)
get_locale_forecast_controller = GetLocaleForecastController(get_locale_forecast_usecase)

@app.route('/auth/signup', methods=['POST'])
def signup_user():
    result = signup_controller.handle(request.json)

    return jsonify(result)

@app.route('/auth/signin', methods=['POST'])
def signin_user():
    result = signin_controller.handle(request.json)

    return jsonify(result)

@app.route('/forecast', methods=['POST'])
def get_forecast():
    result = get_locale_forecast_controller.handle(request.json)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)