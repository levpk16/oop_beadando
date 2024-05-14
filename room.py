from abc import ABC, abstractmethod

class Room(ABC):
    @abstractmethod
    def __init__(self, price, room_number):
        self.price = price
        self.room_number = room_number

    @abstractmethod
    def __str__(self):
        return f"Roomnumber : {self.room_number}, Price is: {self.price}$"