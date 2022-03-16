import plant
import animal
class SosnowskyHogweed(plant.Plant):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "green")
        self.strength = 10
        self.initiative = 0
        self.species = "sosnowskyHogweed"
    def collision(self, organism):
        if organism.mecha == False:
            organism.poisoned = True
    def action(self):
        self.sow()
        spots = self.world.GetPossibleSpots(self.x, self.y, 1)
        for pos in spots:
            x = pos[0]
            y = pos[1]
            if self.world.map[x][y] is not None:
                if isinstance(self.world.map[x][y], animal.Animal) and self.world.map[x][y].mecha == False:
                    self.world.removeOrganism(x, y)
