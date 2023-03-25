from .base import BaseController, T

from domain.usecases.signup_user import SignupUser

class SignupController(BaseController):
    def __init__(self, usecase: SignupUser) -> None:
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

        signup_dto = {
            'username': username,
            'password': password
        }

        try:
            self.usecase.execute(signup_dto)

            return {
                'status': 'ok'
            }
        except Exception as e:
            return {
                'error': e.message
            }
