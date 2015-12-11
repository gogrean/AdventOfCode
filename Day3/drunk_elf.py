import numpy as np

f = open('santas_walk.dat', 'r')
steps = f.read().strip()

coords = set([(0,0)])
last_coord = (0,0)

moves = {
  '^': (0,1),
  '>': (1,0),
  'v': (0,-1),
  '<': (-1,0)
}

for step in steps:
    if step not in moves:
        print("Santa got lost here. Can't understand step: ", step)
        break
    else:
        new_coord = (last_coord[0] + moves[step][0], last_coord[1] + moves[step][1])
        coords.add(new_coord)
        last_coord = new_coord

print('Santa left presents at ', len(coords), ' houses.')


############


coords = set([(0,0)])
last_coord1 = (0,0)
last_coord2 = (0,0)

i = 0
while i <= len(steps)-2:
    if steps[i] not in moves:
        print("Santa got lost here. Can't understand step: ", steps[i])
        break
    elif steps[i+1] not in moves:
        print("Robo-Santa got lost here. Can't understand step: ", steps[i+1])
        break
    else:
        new_coord1 = (last_coord1[0] + moves[steps[i]][0], last_coord1[1] + moves[steps[i]][1])
        coords.add(new_coord1)
        last_coord1 = new_coord1
        new_coord2 = (last_coord2[0] + moves[steps[i+1]][0], last_coord2[1] + moves[steps[i+1]][1])
        coords.add(new_coord2)
        last_coord2 = new_coord2
    i += 2

if i == len(steps)+1:
        new_coord1 = (last_coord1[0] + moves[steps[i-2]][0], last_coord1[1] + moves[steps[i-2]][1])
        coords.add(new_coord1)
  
print('Santa and Robo-Santa left presents at ', len(coords), ' houses.')


















    
