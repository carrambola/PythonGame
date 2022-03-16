import animal
class Human(animal.Animal):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "orange")
        self.strength = 5
        self.initiative = 4
        self.species = "human"
        self.turnCounter = 0
    def action(self):
        if self.turnCounter > 5:
            self.purification()
        if self.turnCounter > 0:
            self.turnCounter -= 1
        direction = self.world.lastKey
        targetX = self.x
        targetY = self.y
        if direction == "u":
            targetY -= 1
        if direction == "d":
            targetY += 1
        if direction == "r":
            targetX += 1
        if direction == "l":
            targetX -= 1
        if direction == "s":
            if self.turnCounter == 0:
                self.turnCounter = 10
            return
        if targetX >= 0 and targetY >= 0 and targetX < self.world.width and targetY < self.world.height:
            self.world.moveOrganism(self, targetX, targetY)
    def purification(self):
        spots = self.world.GetPossibleSpots(self.x, self.y, 1)
        for pos in spots:
            x = pos[0]
            y = pos[1]
            if self.world.map[x][y] is not None:
                self.world.removeOrganism(x, y)
