from room import Room

class Single_Room(Room):
    def __init__(self, room_number, balcony):
        super().__init__(15000, room_number)
        self.balcony = balcony

    def __str__(self):
        return super().__str__() + f", Has balcony: {self.balcony}"
