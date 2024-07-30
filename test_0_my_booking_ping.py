import pytest
import requests
import allure


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking service')
@allure.suite('Ping tests')
@allure.title('Health Check Endpoint')
@allure.description('This test checks the health status of the RESTful Booker service by calling the ping endpoint')
@allure.severity('BLOCKER')
def test_health_check():
    with allure.step('Send a GET request to the server'):
        response = requests.get('https://restful-booker.herokuapp.com/ping')

    with allure.step('Verify the status code of the response'):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'

