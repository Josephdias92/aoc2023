import sys
import re

numbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    
}

def sort_by_key(kv_pair):
    key, value = kv_pair
    return key

def replace_with_number(input: str, numbers: dict):
    temp = {}
    for key, value in numbers.items():
        ind = -1
        while 1:
            ind = input.find(key, ind + 1)
            if (ind <0):
                break
            else:
                temp[ind] = value   
    sorted_values = [value for key, value in sorted(temp.items(), key=sort_by_key)]
    return [sorted_values[0], sorted_values[-1]]




i = open(sys.argv[1], 'r')

d = i.read().splitlines()
total=0
for param in d:
    output = replace_with_number(param, numbers)
    total += int(''.join(map(str, output)))
print(total)

