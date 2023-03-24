import pytest

from src.domain.usecases.signin_user import SigninUser

from src.domain.exceptions.user_not_found import UserNotFound

from tests.mocks.repositories.user import InMemoryUserRepository

repository = InMemoryUserRepository()
signin_usecase = SigninUser(repository)

def test_signin_user():
    input = {
        'username': 'foo',
        'password': 'bar'
    }

    token = signin_usecase.execute(input)

    assert token is not None
    assert type(token) == str

def test_user_not_found():
    input = {
        'username': 'bar',
        'password': 'foo'
    }

    with pytest.raises(UserNotFound) as e:
        signin_usecase.execute(input)

    assert str(e.value) == 'user bar not found'