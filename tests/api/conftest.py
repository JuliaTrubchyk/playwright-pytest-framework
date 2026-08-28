
import pytest
import requests

from api.booking_client import BookingAPIClient
from api.builders import make_booking

BASE_URL = "https://restful-booker.herokuapp.com"

class ApiSession(requests.Session):      # adds base URL + default timeout
    def request(self, method, url, **kwargs):
        kwargs.setdefault("timeout", 10)
        return super().request(method, BASE_URL + url, **kwargs)

@pytest.fixture(scope="session")
def api_session():
    session =  ApiSession()
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()


@pytest.fixture(scope="session")
def auth_token(api_session) -> str:
    r = api_session.post(
        f"/auth",
        json={
            "username": "admin",
            "password": "password123"
        }
    )
    return r.json()["token"]


@pytest.fixture
def booking_client(api_session, auth_token):
    return BookingAPIClient(api_session, auth_token) 


@pytest.fixture
def created_booking(booking_client):
    payload = make_booking()                            # returns body content in form of python dict

    response = booking_client.create_booking(payload)   # returns a Response object — not JSON and not a dictionary.
    response_body = response.json()                     # requests library parses JSON response and gives the equivalent Python dictionary
    booking_id = response_body["bookingid"]

    yield booking_id, payload                           # fixture gives two values to the test. Payload is a Python dictionary

    booking_client.delete_booking(booking_id)           #