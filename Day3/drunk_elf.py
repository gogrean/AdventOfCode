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
        print('Santa got lost here. Last step: ', step)
        break
    else:
        new_coord = (last_coord[0] + moves[step][0], last_coord[1] + moves[step][1])
        coords.add(new_coord)
        last_coord = new_coord

print('Santa left presents at ', len(coords), ' houses.')

############


