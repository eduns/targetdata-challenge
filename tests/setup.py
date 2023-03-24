import pytest

from tests.mocks.repositories.user import InMemoryUserRepository
from tests.mocks.repositories.forecast import InMemoryForecastRepository

from src.domain.usecases.signup_user import SignupUser
from src.domain.usecases.signin_user import SigninUser
from src.domain.usecases.get_locale_forecast import GetLocaleForecast

from src.app.controllers.signup import SignupController
from src.app.controllers.signin import SigninController
from src.app.controllers.get_locale_forecast import GetLocaleForecastController

@pytest.fixture
def setup_signup_controller():
    repository = InMemoryUserRepository()
    usecase = SignupUser(repository)
    controller = SignupController(usecase)

    return controller

@pytest.fixture
def setup_signin_controller():
    repository = InMemoryUserRepository()
    usecase = SigninUser(repository)
    controller = SigninController(usecase)

    return controller

@pytest.fixture
def setup_get_forecast_controller():
    repository = InMemoryForecastRepository()
    usecase = GetLocaleForecast(repository)
    controller = GetLocaleForecastController(usecase)

    return controller
