import pytest
import requests
import allure

import test_1_my_booking_token
import test_2_my_booking_post

@allure.feature('Booking service')
@allure.suite('Partial Booking Update')
@allure.title('Partial Update Booking')
@allure.description('This test partially updates an existing booking and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_partial_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={test_1_my_booking_token.my_token}'
    }

    with allure.step('Send PATCH request to partially update the booking'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_my_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f"Expected Status Code 200, but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify the updated firstname'):
        assert body['firstname'] == response_data['firstname']

    with allure.step('Verify the updated lastname'):
        assert body['lastname'] == response_data['lastname']

    with allure.step('Verify totalprice is present in the response'):
        assert 'totalprice' in response_data, "'totalprice' not found in response"

    with allure.step('Verify depositpaid is present in the response'):
        assert 'depositpaid' in response_data, "'depositpaid' not found in response"

    with allure.step('Verify bookingdates is present in the response'):
        assert 'bookingdates' in response_data, "'bookingdates' not found in response"

    with allure.step('Verify checkin date is present in bookingdates'):
        assert 'checkin' in response_data['bookingdates'], "'checkin' not found in 'bookingdates'"

    with allure.step('Verify checkout date is present in bookingdates'):
        assert 'checkout' in response_data['bookingdates'], "'checkout' not found in 'bookingdates'"

    with allure.step('Verify additionalneeds is present in the response'):
        assert 'additionalneeds' in response_data, "'additionalneeds' not found in response"


@allure.feature('Booking Management')
@allure.suite('Partial Booking Update')
@allure.title('Negative Partial Update Booking with Invalid Token')
@allure.description('This test attempts to partially update a booking with an invalid token and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_partial_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token=12312312'
    }

    with allure.step('Send PATCH request to partially update the booking with an invalid token'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_my_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify the response status code is 403'):
        assert response.status_code == 403, f"Expected Status Code 403, but got {response.status_code}"


@allure.feature('Booking Management')
@allure.suite('Partial Booking Update')
@allure.title('Negative Partial Update Booking without Token')
@allure.description('This test attempts to partially update a booking without a token and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_partial_update_without_token_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    with allure.step('Send PATCH request to partially update the booking without a token'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_my_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify the response status code is 403'):
        assert response.status_code == 403, f"Expected Status Code 403, but got {response.status_code}"


