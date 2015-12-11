import numpy as np

f = open('instructions.dat', 'r')
floors = f.read()

floor_up = floors.count('(')
floor_down = floors.count(')')

right_floor = floor_up - floor_down

print('Santa has to go on floor ', right_floor)

level = 0
i = 0
floors = list(floors)
while i < len(floors) and level != -1:
    if floors[i] == '(':
        level = level + 1
    elif floors[i] == ')':
        level = level - 1
    else:
        print('Unexpected command. Are you trying to get Santa lost?!')
    i += 1

if (i == len(floors)) and (level != -1):
    print("Santa never reaches the basement.")
else:
    print("Santa first reaches basement after following step #", i)
