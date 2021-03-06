# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None, monster=None):
        self.name = name
        self.description = description
        self.items = items
        self.monster = monster
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

# tests
# atrium = Room(
#     "Atrium", "A room or court in the center of a home that is skylighted.")

# print(atrium)
# print(atrium.description)
