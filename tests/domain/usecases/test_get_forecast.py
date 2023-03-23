import unittest

from src.domain.repositories.forecast import InMemoryForecastRepository
from src.domain.usecases.get_locale_forecast import GetLocaleForecast

forecast_repository = InMemoryForecastRepository()
get_forecast_usecase = GetLocaleForecast(forecast_repository)

class TestGetForecastUseCase(unittest.TestCase):
    def test_get_forecast(self):
        locale_cep = '01001000'

        locale_forecast = get_forecast_usecase.execute(locale_cep)

        self.assertIsNotNone(locale_forecast)
        self.assertEqual(locale_forecast.locale['cep'], '01001-000')
        self.assertEqual(locale_forecast.locale['address'], 'Praça da Sé')
        self.assertEqual(locale_forecast.locale['complement'], 'lado ímpar')
        self.assertEqual(locale_forecast.locale['neighborhood'], 'Sé')
        self.assertEqual(locale_forecast.locale['name'], 'São Paulo')
        self.assertEqual(locale_forecast.locale['uf'], 'SP')
        self.assertEqual(locale_forecast.locale['ibge_code'], '3550308')
        self.assertEqual(locale_forecast.locale['gia_code'], '1004')
        self.assertEqual(locale_forecast.locale['ddd_code'], '11')
        self.assertEqual(locale_forecast.locale['siafi_code'], '7107')

        self.assertEqual(locale_forecast.forecast['locale_name'], 'São Paulo')
        self.assertEqual(locale_forecast.forecast['locale_uf'], 'SP')
        self.assertEqual(locale_forecast.forecast['updated_at'], '2023-03-22')
        self.assertEqual(locale_forecast.forecast['forecasts'], [
            {
                'date': '2023-03022',
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
        ])

if __name__ == '__main__':
    unittest.main()