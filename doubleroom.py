from room import Room

class Double_Room(Room):
    def __init__(self, room_number, spare_bed):
        super().__init__(25000, room_number)
        self.spare_bed = spare_bed

    def __str__(self):
        return super().__str__() + f", Has spare bed: {self.spare_bed}"

