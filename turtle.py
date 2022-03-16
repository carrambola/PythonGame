import organism
import random
import animal
class Turtle(animal.Animal):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "#03fcc6")
        self.strength = 2
        self.initiative = 1
        self.species = "turtle"
    def action(self):
        if random.randint(0, 3) == 0:
            self.move()
    def collision(self, organism):
        if organism.strength < 5:
            self.dodge = True
