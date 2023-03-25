from ..entities.LocaleForecast import LocaleForecast

from ..repositories.forecast import ForecastRepository

class GetLocaleForecast():
    def __init__(self, repository: ForecastRepository) -> None:
        self.repository = repository

    def execute(self, get_locale_forecast_dto: dict) -> LocaleForecast:
        locale_cep = get_locale_forecast_dto.get('locale_cep')

        return self.repository.get_forecast(locale_cep)