import unittest

from src.domain.repositories.user import InMemoryUserRepository
from src.domain.usecases.signup_user import SignupUser

repository = InMemoryUserRepository()
signup_usecase = SignupUser(repository)

class TestSignupUserUseCase(unittest.TestCase):
    def test_signup_user(self):
        payload = {
            'username': 'foo',
            'password': 'bar'
        }

        signup_usecase.execute(payload)

        user = repository.get(payload)

        self.assertIsNotNone(user)
    
if __name__ == '__main__':
    unittest.main()