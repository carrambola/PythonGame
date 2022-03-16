import organism
import random

class Animal(organism.Organism):
    def __init__(self, world, x, y, color):
        super().__init__(world, x, y, color)
    def move(self):
        spots = self.world.GetPossibleSpots(self.x, self.y, 1)
        if len(spots) == 0:
            return
        pos = spots[random.randint(0, len(spots) - 1)]
        self.world.moveOrganism(self, pos[0], pos[1])
    def action(self):
        self.move()


