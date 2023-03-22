import unittest

from src.domain.repositories.user import InMemoryUserRepository
from src.domain.usecases.signin_user import SigninUser

repository = InMemoryUserRepository()
signin_usecase = SigninUser(repository)

class TestSigninUserUseCase(unittest.TestCase):
    def test_signin_user(self):
        payload = {
            'username': 'foo',
            'password': 'bar'
        }

        token = signin_usecase.execute(payload)

        self.assertIsNotNone(token)
    
if __name__ == '__main__':
    unittest.main()