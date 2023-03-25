import pytest

from src.domain.usecases.get_locale_forecast import GetLocaleForecast

from tests.mocks.repositories.forecast import InMemoryForecastRepository

from src.app.exceptions.locale_not_found import LocaleNotFound

forecast_repository = InMemoryForecastRepository()
get_forecast_usecase = GetLocaleForecast(forecast_repository)

def test_get_forecast():
    input = {
        'locale_cep': '01001000'
    }

    locale_forecast = get_forecast_usecase.execute(input)

    assert locale_forecast is not None
    assert locale_forecast.locale['cep'] == '01001-000'
    assert locale_forecast.locale['address'] == 'Praça da Sé'
    assert locale_forecast.locale['complement'] == 'lado ímpar'
    assert locale_forecast.locale['neighborhood'] == 'Sé'
    assert locale_forecast.locale['name'] == 'São Paulo'
    assert locale_forecast.locale['uf'] == 'SP'
    assert locale_forecast.locale['ibge_code'] == '3550308'
    assert locale_forecast.locale['gia_code'] == '1004'
    assert locale_forecast.locale['ddd_code'] ==  '11'
    assert locale_forecast.locale['siafi_code'] == '7107'

    assert locale_forecast.forecast['locale_name'] == 'São Paulo'
    assert locale_forecast.forecast['locale_uf'] == 'SP'
    assert locale_forecast.forecast['updated_at'] == '2023-03-22'
    assert locale_forecast.forecast['forecasts'] == [
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

def test_locale_not_found():
    input = {
        'locale_cep': '00000000'
    }

    with pytest.raises(LocaleNotFound) as e:
        get_forecast_usecase.execute(input)

    assert str(e.value) == f'locale with cep {input.get("locale_cep")} not found'