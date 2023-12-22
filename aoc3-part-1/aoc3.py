import sys
with open(sys.argv[1], 'r') as file:
    table = file.read().splitlines()

def getNeighbour(arr, i, j):
    neighbours = {}
    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if 0 <= r < len(arr) and 0 <= c < len(arr[r]) and (r, c) != (i, j) and arr[r][c] != '.':
                start = c
                end = c
                while 0 <= start - 1 and arr[r][start - 1].isdigit():
                    start -= 1
                while end < len(arr[r]) and arr[r][end].isdigit():
                    end = end + 1
                uniqueKey="{}-{},{}-{}".format(r,start, r, end);
                neighbours[uniqueKey] = arr[r][start:end]

    return neighbours.values()

def findSymbol(arr, i, j):
    pattern = "@#$%^&*()_=-+<>~/\\"
    return pattern.find(arr[i][j])>=0
        
allNumbers = []
for row in range(len(table)):
    for col in range(len(table[row])):
        if (findSymbol(table, row, col)):
            neighbours = getNeighbour(table, row, col)
            for sublist in neighbours:
                allNumbers.append(int(sublist))
print(sum(allNumbers))