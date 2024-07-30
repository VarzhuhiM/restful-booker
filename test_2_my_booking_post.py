import pytest
import requests
import allure

my_bookingid = 0

@allure.feature('Booking service')
@allure.suite('Create Booking')
@allure.title('Create Booking')
@allure.description('This test creates a new booking and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_create_booking():
    data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create a booking'):
        response = requests.post(
            'https://restful-booker.herokuapp.com/booking',
            json=data,
            headers=headers
        )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify booking ID is present in the response'):
        assert "bookingid" in response_data, "The response does not contain 'bookingid'"

    with allure.step('Verify booking details are present in the response'):
        assert "booking" in response_data, "The response does not contain 'booking'"

    response_booking = response_data['booking']

    with allure.step('Verify the firstname in the booking details'):
        assert 'firstname' in response_booking, "'firstname' not found in response"

    with allure.step('Verify the lastname in the booking details'):
        assert 'lastname' in response_booking, "'lastname' not found in response"

    with allure.step('Verify the totalprice in the booking details'):
        assert 'totalprice' in response_booking, "'totalprice' not found in response"

    with allure.step('Verify the depositpaid in the booking details'):
        assert 'depositpaid' in response_booking, "'depositpaid' not found in response"

    with allure.step('Verify the booking dates are present in the response'):
        assert 'bookingdates' in response_booking, "'bookingdates' not found in response"

    with allure.step('Verify the checkin date in the booking dates'):
        assert 'checkin' in response_booking['bookingdates'], "'checkin' not found in 'bookingdates'"

    with allure.step('Verify the checkout date in the booking dates'):
        assert 'checkout' in response_booking['bookingdates'], "'checkout' not found in 'bookingdates'"

    with allure.step('Verify the additionalneeds in the booking details'):
        assert 'additionalneeds' in response_booking, "'additionalneeds' not found in response"

    with allure.step('Verify the firstname matches the expected value'):
        assert response_booking['firstname'] == data['firstname'], f"Expected firstname to be {data['firstname']}, but got {response_booking['firstname']}"

    with allure.step('Verify the lastname matches the expected value'):
        assert response_booking['lastname'] == data['lastname'], f"Expected lastname to be {data['lastname']}, but got {response_booking['lastname']}"

    with allure.step('Verify the totalprice matches the expected value'):
        assert response_booking['totalprice'] == data['totalprice'], f"Expected totalprice to be {data['totalprice']}, but got {response_booking['totalprice']}"

    with allure.step('Verify the depositpaid matches the expected value'):
        assert response_booking['depositpaid'] == data['depositpaid'], f"Expected depositpaid to be {data['depositpaid']}, but got {response_booking['depositpaid']}"

    with allure.step('Verify the checkin date matches the expected value'):
        assert response_booking['bookingdates']['checkin'] == data['bookingdates']['checkin'], f"Expected checkin to be {data['bookingdates']['checkin']}, but got {response_booking['bookingdates']['checkin']}"

    with allure.step('Verify the checkout date matches the expected value'):
        assert response_booking['bookingdates']['checkout'] == data['bookingdates']['checkout'], f"Expected checkout to be {data['bookingdates']['checkout']}, but got {response_booking['bookingdates']['checkout']}"

    with allure.step('Verify the additionalneeds matches the expected value'):
        assert response_booking['additionalneeds'] == data['additionalneeds'], f"Expected additionalneeds to be {data['additionalneeds']}, but got {response_booking['additionalneeds']}"

    global my_bookingid
    my_bookingid = response_data['bookingid']
