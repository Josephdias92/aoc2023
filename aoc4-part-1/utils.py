import sys
def readFile():
    with open(sys.argv[1], 'r') as file:
        content = file.read()
    return content
