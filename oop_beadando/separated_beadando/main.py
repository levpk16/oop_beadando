from datetime import datetime

from oop_beadando.separated_beadando.hotel import Hotel
from oop_beadando.separated_beadando.singleroom import Single_Room
from oop_beadando.separated_beadando.doubleroom import Double_Room


def get_valid_date(prompt="Enter date (YYYY-MM-DD): "):
    while True:
        date_str = input(prompt)
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if date < datetime.now().date():
                print("Please enter a future date.")
                continue
            return date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def main():
    hotel = Hotel("Русский отель в Москве")
    room1 = Single_Room(101, True)
    room2 = Double_Room(201, True)
    room3 = Single_Room(102, False)
    room4 = Double_Room(202, False)
    room5 = Single_Room(103, True)
    room6 = Double_Room(203, True)
    room7 = Single_Room(104, False)
    room8 = Double_Room(204, False)
    room9 = Single_Room(105, False)
    room10 = Double_Room(205, True)
    room11 = Single_Room(106, True)
    room12 = Double_Room(206, False)
    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)
    hotel.add_room(room4)
    hotel.add_room(room5)
    hotel.add_room(room6)
    hotel.add_room(room7)
    hotel.add_room(room8)
    hotel.add_room(room9)
    hotel.add_room(room10)
    hotel.add_room(room11)
    hotel.add_room(room12)

    # Itt lehet hasonló képpen hozzáadni foglalást
    hotel.book_room(101, datetime.now().date())
    hotel.book_room(201, datetime.now().date())
    hotel.book_room(206, datetime.now().date())
    hotel.book_room(203, datetime.now().date())
    hotel.book_room(106, datetime.now().date())
    hotel.book_room(104, datetime.fromisocalendar(2024,3,5))

    while True:
        print("\nMenu:")
        print("1. Book a room")
        print("2. List rooms with price")
        print("3. Cancel a reservation")
        print("4. List all reservations")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            room_number = int(input("Enter room number: "))
            date = get_valid_date()
            hotel.book_room(room_number, date)
        elif choice == "2":
            hotel.list_rooms()
        elif choice == "3":
            room_number = int(input("Enter room number: "))
            date = get_valid_date()
            hotel.cancel_reservation(room_number, date)
        elif choice == "4":
            hotel.list_reservations()
        elif choice == "5":
            print("Exiting program...(Пока :D)")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")



if __name__ == "__main__":
    main()
