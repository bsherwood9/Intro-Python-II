from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Dagger", "A sharp pointed piece of refined metal.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Lightbulb", "A glass that will illuminate your world."), Item("Gingersnaps", "A tasty treat for an adventurer.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Tooth", "A dragon tooth from a Mongolian Skyreaper.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Compass", "A large compass that only points North.")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Chest", "A chest full of nothing. Was it worth it?")]),
}


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


# Make a new player object that is currently in the 'outside' room.
game_mode = "Playing"
player = Player(input("What is your name, champion?"),
                "Human", "None", room["outside"])
print([item.name for item in player.current_room.items])
# Write a loop that:
print(f"Welcome to your walk through Hell, {player.name.capitalize()}")
while game_mode == "Playing":
    # Prints the current room name
    # Prints the current description (the textwrap module might be useful here).
    print(
        f"You are located {player.current_room.name}. {player.current_room.description}")
    if len(player.current_room.items) > 0:
        print(f"There are the following items in the room :")
        for item in player.current_room.items:
            print(f"{item.name}")

    else:
        print("You see no items in the room.")

# Waits for user input and decides what to do.
    choice = input(
        "Either choose a direction :[n] North, [s] South, [e] East, [w] West, or [q] Quit game or take an action")
    stuff = choice.split()
# If the user enters "q", quit the game.
    if len(stuff) == 1:
        if choice == "q":
            game_mode = "Not playing"
    # If the user enters a cardinal direction, attempt to move to the room there.
        elif choice == "n":
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to
            else:
                print("You can't go that way. Please try another direction.")
        elif choice == "s":
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print("You can't go that way. Please try another direction.")

        elif choice == "e":
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            else:
                print("You can't go that way. Please try another direction.")
        elif choice == "w":
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            else:
                print("You can't go that way. Please try another direction.")
        else:
            print("Please enter a valid command.")
    else:
        if stuff[0].lower() == "take" or stuff[0].lower() == "grab":
            index_item = ([item.name for item in player.current_room.items].index(
                stuff[1].capitalize()))
            player.grab_item(player.current_room.items[index_item])
            print(player.inventory[0])
        elif stuff[0].lower() == "drop":
            index_item_drop = ([item.name for item in player.inventory].index(
                stuff[1].capitalize()))
            player.remove_item(player.inventory[index_item_drop])
        else:
            print("That item doesn't exist")
            # for stuff[1].lower() in player.current_room.items
            # player.grab_item()
# Print an error message if the movement isn't allowed.
#
