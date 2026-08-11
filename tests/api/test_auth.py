import requests


BASE_URL = "https://restful-booker.herokuapp.com"

def test_get_token():
    # Create and send the request (use the appropriate method)
    response = requests.post(
        f"{BASE_URL}/auth",
        json={
            "username": "admin",
            "password": "password123"
        },
        timeout=10,
    )
    # Check actual data
    assert response.status_code == 200
    assert response.json()["token"]


def test_ping():
    response = requests.get(
        f"{BASE_URL}/ping", timeout=10
    )
    assert response.status_code == 201