import pytest
import requests
import allure

import test_1_my_booking_token
import test_2_my_booking_post

@allure.feature('Booking service')
@allure.suite('Booking Update Suite')
@allure.title('Test Update Booking')
@allure.description('This test updates an existing booking and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={test_1_my_booking_token.my_token}'
    }

    with allure.step('Send PUT request to update the booking'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_my_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the updated firstname'):
        assert body['firstname'] == response_data['firstname'], f"Expected firstname to be {body['firstname']}, but got {response_data['firstname']}"

    with allure.step('Verify the updated lastname'):
        assert body['lastname'] == response_data['lastname'], f"Expected lastname to be {body['lastname']}, but got {response_data['lastname']}"

    with allure.step('Verify the updated totalprice'):
        assert body['totalprice'] == response_data['totalprice'], f"Expected totalprice to be {body['totalprice']}, but got {response_data['totalprice']}"

    with allure.step('Verify the updated depositpaid'):
        assert body['depositpaid'] == response_data['depositpaid'], f"Expected depositpaid to be {body['depositpaid']}, but got {response_data['depositpaid']}"

    with allure.step('Verify the updated checkin date'):
        assert body['bookingdates']['checkin'] == response_data['bookingdates']['checkin'], f"Expected checkin to be {body['bookingdates']['checkin']}, but got {response_data['bookingdates']['checkin']}"

    with allure.step('Verify the updated checkout date'):
        assert body['bookingdates']['checkout'] == response_data['bookingdates']['checkout'], f"Expected checkout to be {body['bookingdates']['checkout']}, but got {response_data['bookingdates']['checkout']}"

    with allure.step('Verify the updated additional needs'):
        assert body['additionalneeds'] == response_data['additionalneeds'], f"Expected additionalneeds to be {body['additionalneeds']}, but got {response_data['additionalneeds']}"


@allure.feature('Booking service')
@allure.suite('Booking Update Suite')
@allure.title('Test Negative Update Booking')
@allure.description('This test attempts to update a booking with an invalid token and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token=1231786qweiy'
    }

    with allure.step('Send PUT request to update the booking with an invalid token'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_my_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify the response status code is 403'):
        assert response.status_code == 403, f'Expected Status Code 403, but got {response.status_code}'
