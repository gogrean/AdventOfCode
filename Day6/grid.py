import numpy as np
import re

f = open('instructions.dat')
strings = f.readlines()

grid = np.zeros((1000,1000))

instructions = {
    "on": lambda x: np.ones(np.shape(x)),
    "off": lambda x: np.zeros(np.shape(x)),
    "toggle": lambda x: 1-x
}

for string in strings:
    coords = [int(i) for i in re.findall(r'[0-9]*', string) if i != '']
    if len(coords) != 4:
        print("Incorrect coordinates: ", coords)
        break
    else:
        keyword = [i for i in instructions if i in string]
        if len(keyword) != 1:
            print("Only one action keyword per line allowed. Incorrect action keywords: ", keyword)
            break
        action = instructions[keyword[0]]
        grid[coords[0]:coords[2]+1,coords[1]:coords[3]+1] = action(grid[coords[0]:coords[2]+1,coords[1]:coords[3]+1])

print(len(np.where(grid==1)[1]), " lights are on.")

##########

grid = np.zeros((1000,1000))

instructions = {
    "on": lambda x: x + 1,
    "off": np.vectorize(lambda x: max(x-1, 0)), 
    "toggle": lambda x: x + 2 
}

for string in strings:
    coords = [int(i) for i in re.findall(r'[0-9]*', string) if i != '']
    if len(coords) != 4:
        print("Incorrect coordinates: ", coords)
        break
    else:
        keyword = [i for i in instructions if i in string]
        if len(keyword) != 1:
            print("Only one action keyword per line allowed. Incorrect action keywords: ", keyword)
            break
        action = instructions[keyword[0]]
        grid[coords[0]:coords[2]+1,coords[1]:coords[3]+1] = action(grid[coords[0]:coords[2]+1,coords[1]:coords[3]+1])

print(np.min(grid), np.max(grid))

print("The total brightness is: ", np.sum(grid))



 
