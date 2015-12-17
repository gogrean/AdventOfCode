from itertools import permutations

f = open('distances.dat', 'r')
edges = f.readlines()

towns = set()
distances = dict()

for edge in edges:
    (start, junk, stop, junk, dist) = edge.split()
    towns.update([start, stop])
    distances.setdefault(start, dict())[stop] = dist
    distances.setdefault(stop, dict())[start] = dist

shortestPath = 1e99
longestPath = 0

for townsPerm in permutations(towns):
     pathLen = sum(map(lambda x, y: int(distances[x][y]), townsPerm[0:len(towns)-1], townsPerm[1:len(towns)]))
     if pathLen < shortestPath:
         shortestPath = pathLen
         continue
     if pathLen > longestPath:
         longestPath = pathLen
         continue

print('The shortest distance is ', shortestPath)
print('The longest distance is ', longestPath)

    

