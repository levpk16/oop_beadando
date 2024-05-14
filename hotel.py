from datetime import datetime

from oop_beadando.separated_beadando.reservation import Reservation


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        hotel_str = f"Hotel: {self.name} \n"
        for room in self.rooms:
            hotel_str += str(room) + "\n"
        return hotel_str

    def is_room_booked(self, room, date):
        for reservation in self.reservations:
            if reservation.room == room and reservation.date == date:
                return True
        return False

    def book_room(self, room_number, date):
        for room in self.rooms:
            if room.room_number == room_number:
                if not self.is_room_booked(room, date):
                    reservation = Reservation(self, room, date)
                    self.reservations.append(reservation)
                    print(f"Room {room_number} booked for {date}")
                    return
                else:
                    print(f"Room {room_number} is already booked for {date}")
                    return
            print(f"Room {room_number} not found")


    def cancel_reservation(self, room_number, date):
        for reservation in self.reservations:
            if reservation.room.room_number == room_number and reservation.date == date:
                self.reservations.remove(reservation)
                print(f"Reservation for Room {room_number} on {date} canceled")
                return
        print("Reservation not found")

    def list_reservations(self):
        print("List of reservations:")
        for reservation in self.reservations:
            print(reservation)

    def list_rooms(self):
        print("List of rooms:")
        for room in self.rooms:
            print(room)