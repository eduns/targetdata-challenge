from tests.setup import setup_signin_controller

def test_signin(setup_signin_controller):
    controller = setup_signin_controller

    result = controller.handle({
        'username': 'foo',
        'password': 'bar'
    })

    assert hasattr(result, 'token') is not None
    assert type(result.get('token')) == str

def test_missing_params(setup_signin_controller):
    controller = setup_signin_controller

    result = controller.handle({})

    assert result['error'] == 'missing params: username, password'

def test_user_not_found(setup_signin_controller):
    controller = setup_signin_controller

    result = controller.handle({
        'username': 'bar',
        'password': 'foo'
    })

    assert result['error'] == 'user bar not found'
