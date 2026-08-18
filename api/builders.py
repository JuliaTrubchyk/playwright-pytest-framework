

# function allows modify any parameter separately if needed by passing parameter. Example: make_booking("firstname" : "Kim")
def make_booking(**overrides):
    booking = {
        "firstname" : "Jim",
        "lastname" : "Brown",
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
