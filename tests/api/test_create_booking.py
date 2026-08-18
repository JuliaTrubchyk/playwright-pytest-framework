
from api.booking_client import BookingAPIClient
from api.builders import make_booking
import pytest


def test_create_booking(booking_client: BookingAPIClient):     # method looks for fixture with name booking_client
    payload= make_booking()
    response = booking_client.create_booking(payload)    # returns a Response object — not JSON and not a dictionary.

    assert response.status_code == 200
    assert response.json()["bookingid"] 
    assert response.json()["booking"] == payload

# Negative
def test_create_without_field(booking_client: BookingAPIClient):
    payload = make_booking()
    del payload["bookingdates"]
    r = booking_client.create_booking(payload)
    print(r.status_code) # 400
    assert r.status_code == 500


