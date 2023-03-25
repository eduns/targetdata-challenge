from .base import BaseController, T

from domain.usecases.signin_user import SigninUser

class SigninController(BaseController):
    def __init__(self, usecase: SigninUser) -> None:
        self.usecase = usecase

    def handle(self, input: object) -> T:
        username = input.get('username')
        password = input.get('password')

        missing_params = []

        if username is None:
            missing_params.append('username')

        if password is None:
            missing_params.append('password')

        if len(missing_params) > 0:
            return {
                'error': f'missing params: {", ".join(missing_params)}'
            }

        signin_dto = {
            'username': username,
            'password': password
        }

        try:
            token = self.usecase.execute(signin_dto)

            return {
                'token': token
            }
        except Exception as e:
            return {
                'error': e.message
            }