

from uuid import uuid4

# function allows modify any parameter separately if needed by passing parameter. Example: make_booking("firstname" : "Kim")
def make_booking(**overrides):
    uuid = uuid4().hex[:8]
    booking = {
        "firstname" : f"Jim{uuid}",
        "lastname" : f"Brown{uuid}",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    booking.update(overrides)
    return booking

# Builds dict
