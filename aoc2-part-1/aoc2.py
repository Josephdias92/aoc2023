import sys

class Game:

    def __init__(self, id, sets):
        self.listOfCubes = []
        self.id = id
        self.sets = sets
        self.updateSet(sets)
    
    def updateSet(self, sets): 
        for set in sets:
            cubesDict = {}
            cubes = set.strip().split(', ')
            for cube in cubes:
                v, color = cube.split(' ')
                cubesDict[color] = int(v)
            self.listOfCubes.append(cubesDict)
    def check(self, inp: dict):
        result = []
        for i in self.listOfCubes: 
            for key, value in inp.items():
                if i.get(key) is not None and i.get(key) > value: 
                    return False
        return True

i = open(sys.argv[1], 'r')
d = i.read().splitlines()
allGame = []
for param in d:
    game, values = param.split(':')
    sets = values.split(';')
    g1 = Game(game.split(' ')[-1], sets)
    allGame.append(g1)

total = 0
for game in allGame: 
    if game.check({ 'red':12 ,'green': 13 , 'blue': 14}):
        total += int(game.id)

print(total)    
