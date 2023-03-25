from src.domain.usecases.signup_user import SignupUser

from tests.mocks.repositories.user import InMemoryUserRepository

repository = InMemoryUserRepository()
usecase = SignupUser(repository)

def test_signup_user():
    payload = {
        'username': 'foo2',
        'password': 'bar2'
    }

    usecase.execute(payload)

    user = repository.get(payload)

    assert user is not None