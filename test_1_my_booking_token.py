import requests
import pytest
import allure

my_token = None


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking service')
@allure.suite('Create Token Booking Suite')
@allure.title('Create Authentication Token')
@allure.description('This test creates an authentication token using valid credentials and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
def test_booking_create_token():
    body = {
        "username": "admin",
        "password": "password123"
    }
    headers = {'Content-Type': 'application/json'}

    @allure.step('Send POST request to create authentication token')
    def send_post_request():
        return requests.post(
            'https://restful-booker.herokuapp.com/auth',
            headers=headers,
            json=body
        )

    response = send_post_request()

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step('Verify the response contains a token'):
        assert 'token' in response.json(), 'Token not found in response'

    with allure.step('Verify the token length is greater than 0'):
        assert len(response.json().get('token')) > 0, 'Token length is 0'

    with allure.step('Save the token to the global variable'):
        global my_token
        my_token = response.json().get('token')


