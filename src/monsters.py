class Monster:

    def __init__(self, name, description, attack, health: int = 20):
        self.name = name
        self.health = health
        self.attack = attack
        self.description = description
        self.isDead = False

    def attack_player(self, health, attack):
        if health:
            health = health - attack
            print(
                f"The beast strikes you and injures you gravely. You now have {health} health.")
            return health
