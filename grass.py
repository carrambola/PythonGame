import plant
class Grass(plant.Plant):
    def __init__(self, world, x, y):
        super(Grass, self).__init__(world, x, y, "#69f542")
        self.strength = 0
        self.initiative = 0
        self.species = "grass"
    def action(self):
        self.sow()