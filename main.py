from room import Room

kitchen = Room("kitchen")
ballroom = Room("ballroom")
dininghall= Room("dininghall")

kitchen.set_description ("small and modern")
print(kitchen.link_room(dininghall, "south"))

ballroom.set_description ("large dancing room")
print(ballroom.link_room(dininghall,"east"))


dininghall.set_description ("eating area")
print(dininghall.link_room(kitchen, "north"))
print(dininghall.link_room(ballroom,"west"))

def set_name(self, room_name):
    self.name = room_name
def get_name(self):
    return self.name

dininghall.get_details()