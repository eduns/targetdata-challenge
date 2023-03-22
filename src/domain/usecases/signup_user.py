from werkzeug.security import generate_password_hash

from ..repositories.user import UserRepository

class SignupUser():
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, user_dto: dict) -> None:
        user = {
            'username': user_dto.get('username'),
            'password_hash': generate_password_hash(user_dto.get('password'), method='sha256')
        }

        self.repository.add(user)