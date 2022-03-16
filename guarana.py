import plant
class Guarana(plant.Plant):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "red")
        self.strength = 0
        self.initiative = 0
        self.species = "guarana"
    def collison(self, organism):
        organism.strength += 3

