from jwt import encode
from datetime import datetime, timedelta

from ..repositories.user import UserRepository

from ..exceptions.user_not_found import UserNotFound

class SigninUser():
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, signin_dto: dict) -> str:
        username = signin_dto.get('username')
        password = signin_dto.get('password')

        user = self.repository.get({
            'username': username,
            'password': password
        })

        if not user:
            raise UserNotFound(username)

        secret_key = 'SECRET'
        expires_in = datetime.now() + timedelta(minutes=5)

        token = encode({
            'username': user.get('username'),
            'exp': expires_in
        }, secret_key, algorithm='HS256')

        return token