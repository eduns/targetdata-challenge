from ..entities.LocaleForecast import LocaleForecast
from ..repositories.forecast import ForecastRepository

class GetLocaleForecast():
    def __init__(self, repository: ForecastRepository) -> None:
        self.repository = repository

    def execute(self, locale_cep: str) -> LocaleForecast:
        return self.repository.get_forecast(locale_cep)