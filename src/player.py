# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, race, power, health, current_room,):
        self.name = name
        self.race = race
        self.power = power
        self.health = health
        self.inventory = []
        self.current_room = current_room
        self.isDead = False

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

    def check_inventory(self):
        print("You currently have the following in your inventory: ")
        for item in self.inventory:
            print(f"{item.name} - {item.description}")

    def attack_monster(self, monster):
        print("You lunge at the beast and punch it wildly.")
        mon_health = monster.health - 10
        if mon_health >= 1:
            print("You hurt the beast and it lashes back.")
            newhealth = monster.attack_player(self.health, monster.attack)
            self.health = newhealth
            if self.health <= 0:
                print("You have died.")
                self.isDead = True
            else:
                print("You are injured. Fight or run.")
        else:
            print("You have killed the beast. It lies in its own blood.")
            monster.health = 0
            monster.isDead = True

# tests
# noob = Player("jojo", "orc", "water", "atrium")
# print(noob.name)
# print("hello")
