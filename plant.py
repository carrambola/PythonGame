import organism
import random
class Plant(organism.Organism):
    def __init__(self, world, x, y, color):
        super().__init__(world, x, y, color)
        self.strength = 0
        self.initiative = 0
    def sow(self):
        spots = self.world.GetFreePossibleSpots(self.x, self.y, 1)
        if len(spots) == 0:
            return
        probability = random.random()
        if probability < 0.2:
            pos = spots[random.randint(0, len(spots) - 1)]
            newOrg = self.world.create(self.species)
            newOrg.x = pos[0]
            newOrg.y = pos[1]
            self.world.addOrganism(newOrg)
    def action(self):
        self.sow()