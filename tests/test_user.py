import requests
def test_user_endpoint():
    url = "http://localhost:5500/cse270/teton/1.6/"
    # test admin credentials (empty, code 200)
    params1 = {
        "admin": "admin", "password": "querty"
    }
    responce1 = requests.get(url, params=params1)
    assert responce1.status_code == 200
    assert responce1.text == ""
def test_user_endpoint_invalid_credentials():
    url = "http://localhost:5500/cse270/teton/1.6/"
    # test invalid credentials (code 401)
    params2 = {
        "admin": "invalid", "password": "invalid"
    }
    responce2 = requests.get(url, params=params2)
    assert responce2.status_code == 401
def test_authentication_successful(mocker):
    url = "http://localhost:5500/cse270/teton/1.6/"
    # Mock successful authentication response
    params = {
        "admin": "admin", "password": "querty"
    }
    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ""
    mocker.patch('requests.get', return_value=mocked_response)
    response = requests.get(url, params=params)
    assert response.status_code == 200
    assert response.text.strip() == ""