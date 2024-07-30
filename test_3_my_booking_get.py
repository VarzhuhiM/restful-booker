import allure
import pytest
import requests

import test_2_my_booking_post


@allure.feature('Booking service')
@allure.suite(' Get Bookings suite')
@allure.title('Get all bookings')
@allure.description('This test verifies that the endpoint for retrieving all bookings returns a successful response with a non-empty list.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_all():
    with allure.step('Send a GET request to retrieve all bookings'):
        response = requests.get('https://restful-booker.herokuapp.com/booking')

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step('Verify the response contains a non-empty list'):
        assert len(response.json()) > 0, 'The list should not be empty'


@pytest.mark.regression
@allure.feature('Booking Management')
@allure.suite('Get Bookings')
@allure.title('Get booking by ID')
@allure.description('This test verifies that the endpoint for retrieving a specific booking by ID returns the expected data structure and values.')
@allure.severity(allure.severity_level.NORMAL)
def test_get_booking_by_id():
    with allure.step('Send a GET request to retrieve booking by ID'):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking/{test_2_my_booking_post.my_bookingid}')

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step("Verify 'firstname' is in the response"):
        assert 'firstname' in response_data, "The response does not contain 'firstname'"

    with allure.step("Verify 'lastname' is in the response"):
        assert 'lastname' in response_data, "The response does not contain 'lastname'"


    with allure.step("Verify 'totalprice' is in the response"):
        assert 'totalprice' in response_data, "The response does not contain 'totalprice'"

    with allure.step("Verify 'depositpaid' is in the response"):
        assert 'depositpaid' in response_data, "The response does not contain 'depositpaid'"

    with allure.step("Verify 'bookingdates' is in the response"):
        assert 'bookingdates' in response_data, "The response does not contain 'bookingdates'"

    with allure.step("Verify 'checkin' is in 'bookingdates'"):
        assert 'checkin' in response_data['bookingdates'], "The response does not contain 'checkin'"

    with allure.step("Verify 'checkout' is in 'bookingdates'"):
        assert 'checkout' in response_data['bookingdates'], "The response does not contain 'checkout'"

    with allure.step("Verify 'additionalneeds' is in the response"):
        assert 'additionalneeds' in response_data, "The response does not contain 'additionalneeds'"

    with allure.step("Verify 'depositpaid' is a boolean"):
        assert response_data['depositpaid'] == True or response_data['depositpaid'] == False, 'Error: depositpaid should be boolea'

    with allure.step("Verify 'totalprice' is an integer or float"):
        assert type(response_data['totalprice']) == int or type(response_data['totalprice']) == float, 'Error: totalprice should be an integer or float'



