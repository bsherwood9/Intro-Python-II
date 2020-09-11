from room import Room
from player import Player
from item import Item
from monsters import Monster
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Dagger", "A sharp pointed piece of refined metal.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Lightbulb", "A glass that will illuminate your world."), Item("Gingersnaps", "A tasty treat for an adventurer.")], Monster("Cherubim", "A winged beast with a flaming sword.", 30, 40)),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Tooth", "A dragon tooth from a Mongolian Skyreaper.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Compass", "A large compass that only points North.")], Monster("Wormling", "A small feeble yet angry legged worm.", 5, 10)),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Chest", "A chest full of nothing. Was it worth it?")]),
}

controls = ["N/North", "E/East", "W/West", "S/South", "Q/Quit",
            "A/Attack", "Take [item name]/Grab [item name]", 'Drop [item name]']
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


def room_update(players):
    print(
        f"You are now located {players.current_room.name}. {players.current_room.description}")
    if len(players.current_room.items) > 0:
        print(f"There are the following items in the room :")
        for item in players.current_room.items:
            print(f"\t{item.name}")
    else:
        print("You see no items in the room.")


# Make a new player object that is currently in the 'outside' room.
game_mode = "Playing"
player = Player(input("What is your name, champion? "),
                "Human", "None", 20, room["outside"])
# print([item.name for item in player.current_room.items])
# Write a loop that:
print(
    f"Welcome to your walk through Hell, {player.name.strip().capitalize()}!")
intro = "You awake to find yourself outside at the base of a large mountain. You are in your night clothes with only your slippers. How did you get here? Where are you? What should you do? You must discover these answers for yourself. You set off towards a hole in the mountain side. "

wrapper = textwrap.TextWrapper(width=60)
intro_text = wrapper.wrap(text=intro)
print("")
for el in intro_text:
    print(el)

# start of game
while game_mode == "Playing" and player.isDead == False:

    # Prints the current room name
    # Prints the current description (the textwrap module might be useful here).
    if player.current_room.monster:
        room_update(player)
        if player.current_room.monster.isDead:
            print("")
            print(
                f"You see a bloodied {player.current_room.monster.name}. It appears dead.")
        else:
            print("")
            print("You also notice that a creature is in the room.")
            print(
                f"You see a {player.current_room.monster.name} - {player.current_room.monster.description}")
    else:
        room_update(player)
# Waits for user input and decides what to do.

    choice = input(
        "What would you like to do?")
    search = choice.split()
# If the user enters "q", quit the game.
    if len(search) == 1:
        if choice.lower() in ["q", "quit"]:
            game_mode = "Not playing"
    # If the user enters a cardinal direction, attempt to move to the room there.
        elif choice.lower() in ["n", "north"]:
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to
            else:
                print("You can't go that way. Please try another direction.")
                print("")
        elif choice.lower() == "s":
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print("You can't go that way. Please try another direction.")
                print("")
        elif choice.lower() == "e":
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            else:
                print("You can't go that way. Please try another direction.")
                print("")
        elif choice == "w":
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            else:
                print("You can't go that way. Please try another direction.")
                print("")
        elif choice in ["i", "inventory"]:
            player.check_inventory()
        elif choice.lower() in ["h", "help"]:
            print("You can use the following commands:")
            print("")
            for cmd in controls:
                print(cmd)
        elif choice.lower() in ["attack", "fight"]:
            if player.current_room.monster:
                if player.current_room.monster.health > player.health:
                    sure = input(
                        "The monster is too strong. Are you sure you want to attack?")
                    if sure in ["y", "yes"]:
                        player.attack_monster(player.current_room.monster)
                    else:
                        print("You don't engage with the monster.")
                else:
                    player.attack_monster(player.current_room.monster)

            else:
                print("There is nothing to attack.")
        else:
            print("Please enter a valid command.")
    else:
        if search[0].lower() in ["take", "grab"]:
            search_item = search[1].capitalize()
            for item in player.current_room.items:
                if item.name == search_item:
                    player.grab_item(item)
                    break
            else:
                print("You don't see that item in this room")

        elif search[0].lower() == "drop":
            search_item = search[1].capitalize()
            for item in player.inventory:
                if item.name == search_item:
                    player.remove_item(item)
                    break
            else:
                print("You don't currently have that item.")
        else:
            print("That action isn't possible.")
            # for stuff[1].lower() in player.current_room.items
            # player.grab_item()
# Print an error message if the movement isn't allowed.
#

# This is what I did before.
# if [item.name for item in player.current_room.items if item.name == search[1].capitalize()]:
            #     index_item = ([item.name for item in player.current_room.items].index(
            #         search[1].capitalize()))
            #     player.grab_item(player.current_room.items[index_item])
            #     print(player.inventory[0])
