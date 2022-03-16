import tkinter
import organism
import sheep
import wolf
import turtle
import fox
import antelope
import human
import cyberSheep
import grass
import belladonna
import guarana
import sowThistle
import sosnowskyHogweed
import random
class World:
    def __init__(self, window, width, height):
        self.organisms = []
        for i in range(8):
            self.organisms.append([])
        self.window= window
        self.width = width
        self.height = height
        self.canvas = tkinter.Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        self.map = []
        for i in range(width):
            self.map.append([])
            for j in range(height):
                self.map[i].append(None)
        self.lastKey = ""

    def generateOrganisms(self):
        self.addOrganism(grass.Grass(self, 1, 2))
        self.addOrganism(belladonna.Belladonna(self, 5, 2))
        self.addOrganism(guarana.Guarana(self, 10, 2))
        self.addOrganism(sowThistle.SowThistle(self, 8, 12))
        self.addOrganism(sosnowskyHogweed.SosnowskyHogweed(self, 16, 1))

        self.addOrganism(sheep.Sheep(self, 16, 9))
        self.addOrganism(wolf.Wolf(self, 5, 6))
        self.addOrganism(turtle.Turtle(self, 7, 8))
        self.addOrganism(fox.Fox(self, 9, 10))
        self.addOrganism(antelope.Antelope(self, 11, 12))
        self.addOrganism(cyberSheep.CyberSheep(self, 13, 14))
        self.addOrganism(sheep.Sheep(self, 16, 10))
        self.addOrganism(wolf.Wolf(self, 12, 6))
        self.addOrganism(turtle.Turtle(self, 3, 8))
        self.addOrganism(fox.Fox(self, 10, 10))
        self.addOrganism(antelope.Antelope(self, 1, 12))
        self.addOrganism(cyberSheep.CyberSheep(self, 4, 14))

        self.addOrganism(human.Human(self, 15, 6))
    def draw(self):
        self.canvas.delete("all")
        #canvas.create_rectangle(50, 0, 100, 40, fill = "red")
        for list in self.organisms:
            for org in list:
                self.canvas.create_rectangle(org.x*20, org.y*20, org.x*20+20, org.y*20 + 20, fill=org.color)
    def step(self):
        for i in range(len(self.organisms)-1, -1, -1):
            list = self.organisms[i]
            for j in list:
                j.ready = True
        for i in range(len(self.organisms)-1, -1, -1):
            list = self.organisms[i]
            for j in list:
                if j.ready:
                    j.action()


        self.draw()
    def key(self, event):
        self.lastKey = ""
        if event.keycode == 38:
            self.lastKey = "u"
        if event.keycode == 39:
            self.lastKey = "r"
        if event.keycode == 40:
            self.lastKey = "d"
        if event.keycode == 37:
            self.lastKey = "l"
        if event.keycode == 32:
            self.lastKey = "s"
        if event.keycode == 83:
            self.saveGame()
        if event.keycode == 76:
            self.loadGame()
            self.draw()
            return
        if self.lastKey == "":
            return
        self.step()
    def GetPossibleSpots(self, x, y, r):
        spots = []
        for i in range(-r, r+1):
            for j in range(-r, r+1):
                if not (i == 0 and j == 0):
                    if x + i >= 0 and x + i < self.width and y + j >= 0 and y + j < self.height:
                        spots.append((x + i, y + j))
        return spots
    def GetFreePossibleSpots(self, x, y, range):
        spots = self.GetPossibleSpots(x, y, range)
        filtered = []
        for position in spots:
            posX, posY = position
            if self.map[posX][posY] is None:
                filtered.append(position)
        return filtered
    def GetFreeWeakerPossibleSpots(self, x, y, range, str):
        spots = self.GetPossibleSpots(x, y, range)
        filtered = []
        for position in spots:
            posX, posY = position
            if self.map[posX][posY] is None or self.map[posX][posY].strength < str:
                filtered.append(position)
        return filtered
    def addOrganism(self, organism: organism.Organism):
        x = organism.x
        y = organism.y
        self.map[x][y] = organism
        self.organisms[organism.initiative].append(organism)
    def removeOrganism(self, x, y):
        if self.map[x][y] is not None:
            org = self.map[x][y]
            self.map[x][y] = None
            self.organisms[org.initiative].remove(org)
    def moveOrganism(self, organism, x, y):
        if self.map[x][y] == None:
            self.map[x][y] = organism
            self.map[organism.x][organism.y] = None
            organism.x = x
            organism.y = y
        elif self.map[x][y].species != organism.species:
            defender = self.map[x][y]
            defender.collision(organism)
            if defender.dodge:
                defender.dodge = False
                return
            if defender.strength > organism.strength:
                self.removeOrganism(organism.x,organism.y)
            else:
                self.removeOrganism(x, y)
                if organism.poisoned:
                    self.removeOrganism(organism.x, organism.y)
                else:
                    self.moveOrganism(organism, x, y)
        else:
            spots = self.GetFreePossibleSpots(organism.x, organism.y, 1)
            if len(spots) == 0:
                return
            pos = spots[random.randint(0, len(spots) - 1)]
            newOrg = self.create(organism.species)
            newOrg.x = pos[0]
            newOrg.y = pos[1]
            self.addOrganism(newOrg)


    def create(self, species):
        if species == "grass":
            return grass.Grass(self, 0, 0)
        if species == "sowThistle":
            return sowThistle.SowThistle(self, 1, 1)
        if species == "sosnowskyHogweed":
            return sosnowskyHogweed.SosnowskyHogweed(self, 2, 2)
        if species == "belladonna":
            return belladonna.Belladonna(self, 3, 3)
        if species == "guarana":
            return guarana.Guarana(self, 4, 4)
        if species == "wolf":
            return wolf.Wolf(self, 5, 5)
        if species == "sheep":
            return sheep.Sheep(self, 6, 6)
        if species == "cyberSheep":
            return cyberSheep.CyberSheep(self, 7, 7)
        if species == "turtle":
            return turtle.Turtle(self, 8, 8)
        if species == "antelope":
            return antelope.Antelope(self, 9, 9)
        if species == "fox":
            return fox.Fox(self, 10, 10)
        if species == "human":
            return human.Human(self, 11, 11)
    def GetNearestHogweed(self, x, y):
        org = None
        minDistance = self.width
        for i in range(self.width):
            for j in range(self.height):
                if self.map[i][j] == None:
                    continue
                if self.map[i][j].species == "sosnowskyHogweed":
                    if min(abs(x-i), abs(y-j)) < minDistance:
                        minDistance = min(abs(x-i), abs(y-j))
                        org = self.map[i][j]
        return org
    def saveGame(self):
        file = open("save.txt", "w")
        file.write(str(self.width))
        file.write(" ")
        file.write(str(self.height))
        file.write("\n")
        for list in self.organisms:
            for org in list:
                file.write(org.species)
                file.write(" ")
                file.write(str(org.x))
                file.write(" ")
                file.write(str(org.y))
                file.write(" ")
                file.write(str(org.strength))
                file.write(" ")
                if org.species == "human":
                    file.write(str(org.turnCounter))
                file.write("\n")
        file.close()
    def loadGame(self):
        file = open("save.txt", "r")
        lines = file.readlines()
        l = lines[0].split(" ")
        w = int(l[0])
        h = int(l[1])
        self.width = w
        self.height = h
        self.organisms = []
        for i in range(8):
            self.organisms.append([])
        self.map = []
        for i in range(self.width):
            self.map.append([])
            for j in range(self.height):
                self.map[i].append(None)
        lines = lines[1:]
        for line in lines:
            line = line.split(" ")
            org = self.create(line[0])
            x = int(line[1])
            y = int(line[2])
            s = int(line[3])
            org.setX(x)
            org.setY(y)
            org.setStrength(s)
            if line[0] == "human":
                t = int(line[4])
                org.turnCounter = t
            self.addOrganism(org)
        file.close()




















