from tests.setup import setup_signup_controller

def test_signup(setup_signup_controller):
    controller = setup_signup_controller

    result = controller.handle({
        'username': 'foo',
        'password': 'bar'
    })

    assert result.get('status') is not None
    assert result.get('status') == 'ok'

def test_missing_params(setup_signup_controller):
    controller = setup_signup_controller

    result = controller.handle({})

    assert result.get('error') == 'missing params: username, password'
