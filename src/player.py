# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, race, power, current_room):
        self.name = name
        self.race = race
        self.power = power
        self.current_room = current_room


noob = Player("jojo", "orc", "water", "atrium")
print(noob.name)
print("hello")
