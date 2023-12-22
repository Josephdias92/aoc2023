import utils

content = utils.readFile()

lines = content.splitlines()
values = [line.split(': ') for line in lines]

def checkIfWon(win:set, drawn):
    count = 0
    for d in drawnNumber:
        if d in win:
            if count == 0:
                count = 1
            else:
                count *= 2
    return count

count = 0
for winning, numbers in (v[1].split('|') for v in values):
    winningSet = set(winning.split())
    drawnNumber = list(numbers.split())
    count += checkIfWon(winningSet, drawnNumber)
print(count)