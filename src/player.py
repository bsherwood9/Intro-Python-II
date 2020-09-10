# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, race, power, current_room,):
        self.name = name
        self.race = race
        self.power = power
        self.inventory = []
        self.current_room = current_room

    def grab_item(self, item):
        self.inventory.append(item)
        self.current_room.items.remove(item)
        print(f"You've picked up a {item.name}")
        print(
            f"You have {self.inventory[len(self.inventory)-1].name} in your inventory.")

    def remove_item(self, item):
        self.inventory.remove(item)
        self.current_room.items.append(item)
        print(f"You've dropped a {item.name}")
        print(
            f"You have {str(len(self.inventory))} items left in your inventory.")


noob = Player("jojo", "orc", "water", "atrium")
print(noob.name)
print("hello")
