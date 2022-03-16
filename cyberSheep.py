import animal
import random
class CyberSheep(animal.Animal):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, "#00b8cc")
        self.strength = 11
        self.initiative = 4
        self.mecha = True
        self.species = "cyberSheep"
    def action(self):
        hogweed = self.world.GetNearestHogweed(self.x, self.y)
        tx = self.x
        ty = self.y
        if hogweed == None:
            self.move()
        else:
            if hogweed.x < self.x:
                tx -= 1
            if hogweed.x > self.x:
                tx += 1
            if hogweed.y < self.y:
                ty -= 1
            if hogweed.y > self.y:
                ty += 1
            self.world.moveOrganism(self, tx, ty)

