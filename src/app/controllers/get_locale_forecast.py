from .base import BaseController, T

from domain.usecases.get_locale_forecast import GetLocaleForecast

class GetLocaleForecastController(BaseController):
    def __init__(self, usecase: GetLocaleForecast) -> None:
        self.usecase = usecase

    def handle(self, input: object) -> T:
        locale_cep = input.get('locale_cep')

        if not locale_cep:
            return {
                'error': 'missing param: locale_cep'
            }

        get_locale_forecast_dto = {
            'locale_cep': locale_cep
        }

        try:
            locale_forecast = self.usecase.execute(get_locale_forecast_dto)

            return {
                'locale': locale_forecast.locale,
                'forecast': locale_forecast.forecast
            }
        except Exception as e:
            return {
                'error': e.message
            }