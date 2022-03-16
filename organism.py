import world
class Organism:
    def __init__(self, world, x, y, color):
        self.world = world
        self.x = x
        self.y = y
        self.color = color
        self.initiative = 0
        self.strength = 0
        self.poisoned = False
        self.dodge = False
        self.ready  = False
        self.mecha = False
    def  getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def action(self):
        pass
    def collision(self, organism):
        pass
    def setStrength(self, strength):
        self.strength = strength

