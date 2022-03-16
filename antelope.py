
import animal
import random
class Antelope(animal.Animal):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "brown")
        self.strength = 4
        self.initiative = 4
        self.species = "antelope"
    def move(self):
        spots = self.world.GetPossibleSpots(self.x, self.y, 2)
        if len(spots) == 0:
            return
        pos = spots[random.randint(0, len(spots) - 1)]
        self.world.moveOrganism(self, pos[0], pos[1])
    def collision(self, organism):
        if random.randint(0, 1) == 0:
            self.dodge = True
            spots = self.world.GetFreePossibleSpots(self.x, self.y, 1)
            if len(spots) == 0:
                return
            pos = spots[random.randint(0, len(spots) - 1)]
            self.world.moveOrganism(self, pos[0], pos[1])
