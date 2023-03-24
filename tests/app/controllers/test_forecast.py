from tests.setup import setup_get_forecast_controller

def test_get_forecast(setup_get_forecast_controller):
    controller = setup_get_forecast_controller

    result = controller.handle({
        'locale_cep': '01001000'
    })

    assert result.get('locale') is not None
    assert result.get('forecast') is not None

def test_missing_param(setup_get_forecast_controller):
    controller = setup_get_forecast_controller

    result = controller.handle({})

    assert result.get('error') is not None
    assert result.get('error') == 'missing param: locale_cep'

def test_locale_not_found(setup_get_forecast_controller):
    controller = setup_get_forecast_controller

    input = {
        'locale_cep': '00000000'
    }

    result = controller.handle(input)

    assert result.get('error') is not None
    assert result.get('error') == f'locale with cep {input.get("locale_cep")} not found'
