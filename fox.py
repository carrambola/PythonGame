import animal
import random
class Fox(animal.Animal):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "pink")
        self.strength = 3
        self.initiative = 7
        self.species = "fox"
    def move(self):
        spots = self.world.GetFreeWeakerPossibleSpots(self.x, self.y, 1, self.strength)
        if len(spots) == 0:
            return
        pos = spots[random.randint(0, len(spots) - 1)]
        self.world.moveOrganism(self, pos[0], pos[1])
