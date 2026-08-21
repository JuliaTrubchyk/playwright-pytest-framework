

from api.booking_client import BookingAPIClient
from api.builders import make_booking


def test_deleted_booking_is_gone(booking_client:BookingAPIClient, created_booking):
    booking_id, payload = created_booking
    response = booking_client.delete_booking(booking_id)

    assert response.status_code == 201
    assert booking_client.get_booking(booking_id).status_code == 404

def test_delete_without_token(api_session, created_booking):
    booking_id, payload = created_booking

    anonymous = BookingAPIClient(api_session)
    r = anonymous.delete_booking(booking_id)
    assert r.status_code == 403

def test_full_booking_cycle(booking_client:BookingAPIClient):
    # Create
    payload = make_booking()
    booking_id = booking_client.create_booking(payload).json()["bookingid"]
    # Read
    assert booking_client.get_booking(booking_id).json() == payload
    # Update
    new_payload = make_booking(totalprice=999)
    booking_client.update_booking(booking_id, new_payload)
    assert booking_client.get_booking(booking_id).json() == new_payload
    # Delete
    booking_client.delete_booking(booking_id)
    assert booking_client.get_booking(booking_id).status_code == 404