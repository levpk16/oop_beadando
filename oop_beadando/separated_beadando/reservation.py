class Reservation:
    def __init__(self, hotel, room, date):
        self.hotel = hotel
        self.room = room
        self.date = date

    def __str__(self):
            return f"Booking at {self.hotel.name} on {self.date} for room {self.room.room_number}" + ("\n")

