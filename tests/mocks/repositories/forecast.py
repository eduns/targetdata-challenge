from src.domain.entities.LocaleForecast import LocaleForecast

from src.domain.repositories.forecast import ForecastRepository

from src.app.exceptions.locale_not_found import LocaleNotFound

class InMemoryForecastRepository(ForecastRepository):
    def __init__(self) -> None:
        self.ceps = {
            '01001000': {
                'cep': '01001-000',
                'address': 'Praça da Sé',
                'complement': 'lado ímpar',
                'neighborhood': 'Sé',
                'name': 'São Paulo',
                'uf': 'SP',
                'ibge_code': '3550308',
                'gia_code': '1004',
                'ddd_code': '11',
                'siafi_code': '7107'
            }
        }

        self.locales = {
            'São Paulo': {
                'id': '244'
            }
        }

        self.forecasts = {
            '244': {
                'locale_name': 'São Paulo',
                'locale_uf': 'SP',
                'updated_at': '2023-03-22',
                'forecasts': [
                    {
                        'date': '2023-03-22',
                        'weather': 'pn',
                        'max': '28',
                        'min': '18',
                        'iuv': '10.0'
                    },
                    {
                        'date': '2023-03-23',
                        'weather': 'pn',
                        'max': '28',
                        'min': '18',
                        'iuv': '10.0'
                    },
                    {
                        'date': '2023-03-24',
                        'weather': 'ci',
                        'max': '29',
                        'min': '18',
                        'iuv': '10.0'
                    },
                    {
                        'date': '2023-03-25',
                        'weather': 'pn',
                        'max': '28',
                        'min': '18',
                        'iuv': '10.0'
                    }
                ]
            }
        }

    def get_forecast(self, locale_cep: str) -> LocaleForecast:
        locale_data = self.ceps.get(locale_cep)

        if not locale_data:
            raise LocaleNotFound(locale_cep)

        locale_name = locale_data['name']
        locale_id = self.locales[locale_name]['id']

        forecast_data = self.forecasts[locale_id]

        return LocaleForecast(locale_data, forecast_data)