from jwt import encode
from datetime import datetime, timedelta

from ..repositories.user import UserRepository

class SigninUser():
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, user_dto: dict) -> str | None:
        user = self.repository.get(user_dto)

        secret_key = 'SECRET'
        expires_in = datetime.now() + timedelta(minutes=5)

        token = encode({
            'username': user.get('username'),
            'exp': expires_in
        }, secret_key, algorithm='HS256')

        return token