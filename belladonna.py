import plant
class Belladonna(plant.Plant):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "violet")
        self.strength = 99
        self.initiative = 0
        self.species = "belladonna"
    def collision(self, organism):
        organism.poisoned = True

