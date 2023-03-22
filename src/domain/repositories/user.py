from abc import ABC, abstractmethod
from werkzeug.security import check_password_hash

class UserRepository(ABC):
    @abstractmethod
    def get(self) -> dict:
        pass

    @abstractmethod
    def add(self, user: dict) -> None:
        pass

class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self.db = {
            'users': {
                'foo': {
                    'username': 'foo',
                    'password_hash': 'sha256$9Jjk5Boe2gatZOEu$9cf8e8e513e5c68c44b2dd500fe511acc5de93856a9c45b7a065e1c8e3c7980e'
                }
            }
        }

    def get(self, user_data: dict) -> dict | None:
        user = self.db['users'].get(user_data.get('username'))

        if user and check_password_hash(user.get('password_hash'), user_data.get('password')):
            return user

    def add(self, user: dict) -> None:
        self.db['users'][user.get('username')] = {
            'username': str(user.get('username')),
            'password_hash': str(user.get('password_hash'))
        }