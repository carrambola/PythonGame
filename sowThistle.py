import plant
class SowThistle(plant.Plant):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "yellow")
        self.strength = 0
        self.initiative = 0
        self.species = "sowThistle"
    def action(self):
        self.sow()
        self.sow()
        self.sow()
