import requests
import pytest
import allure

import test_1_my_booking_token
import test_2_my_booking_post


@allure.feature('Booking Management')
@allure.suite('Delete Booking')
@allure.title('Delete Booking by ID')
@allure.description('This test deletes a booking by ID and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_booking_by_id():
    headers = {'Content-Type': 'application/json', 'Cookie': f'token={test_1_my_booking_token.my_token}'}

    with allure.step('Send DELETE request to delete a booking'):
        response = requests.delete(
            f'https://restful-booker.herokuapp.com/booking/{test_2_my_booking_post.my_bookingid}',
            headers=headers
        )

    with allure.step('Verify the response status code is 201'):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'
