import numpy as np

f = open('present_info.dat', 'r')

paper = 0
ribbon = 0
for line in f:
    dim = line.split('x')
    if len(dim) != 3:
        print('Incorrect box dimensions: ', dim)
        break
    dim[0], dim[1], dim[2] = int(dim[0]), int(dim[1]), int(dim[2])

    areas = [dim[0]*dim[1], dim[1]*dim[2], dim[2]*dim[0]]
    paper += 2*np.sum(areas)
    paper += np.min(areas)
    
    volume = dim[0]*dim[1]*dim[2]
    perimeter = np.min([dim[0]+dim[1], dim[1]+dim[2], dim[2]+dim[0]])
    ribbon += 2*perimeter + volume

print('The area of the wrapping paper required by the elves is ', paper, ' sq ft.')
print('The length of ribbon required by the elves to make perfect bows is ', ribbon, ' ft.')
