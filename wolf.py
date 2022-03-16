import animal
class Wolf(animal.Animal):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "grey")
        self.strength = 9
        self.initiative = 5
        self.species = "wolf"