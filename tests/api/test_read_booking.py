

from api.booking_client import BookingAPIClient


def test_created_booking_reads(booking_client:BookingAPIClient, created_booking):
    
    booking_id, payload  = created_booking

    response = booking_client.get_booking(booking_id)
    assert response.status_code == 200
    assert response.json() == payload


def test_missing_booking_id(booking_client:BookingAPIClient):

    response = booking_client.get_booking(9999)
    assert response.status_code == 404


def test_booking_appears_in_ids(booking_client : BookingAPIClient, created_booking):
    booking_id, payload  = created_booking

    rows = booking_client.get_booking_ids().json()
    ids = [row["bookingid"] for row in rows]
    assert booking_id in ids





# GetBookingIds       /booking
def  test_json(booking_client : BookingAPIClient):
    rows = booking_client.get_booking_ids().json()
    # print(rows.json())

    # print(rows[0])

    for row in rows[:100]:
        print(row["bookingid"])


