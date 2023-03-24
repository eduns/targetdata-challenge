from ..repositories.user import UserRepository

class SignupUser():
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, signup_dto: dict) -> None:
        username = signup_dto.get('username')
        password = signup_dto.get('password')

        self.repository.add({
            'username': username,
            'password': password
        })