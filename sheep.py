import animal
class Sheep(animal.Animal):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "white")
        self.strength = 4
        self.initiative = 4
        self.species = "sheep"
    def action(self):
        self.move()