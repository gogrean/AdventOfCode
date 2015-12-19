from itertools import permutations

f = open('happiness_info.dat', 'r')
edges = f.readlines()

people = set()
happiness = dict()

for edge in edges:
    edge = edge.replace('.', '')
    info = edge.split()
    person1 = info[0]
    person2 = info[10]
    happy = int(info[3])
    if info[2] == 'lose':
        happy = -happy
    people.update([person1, person2])
    happiness.setdefault(person1, dict())[person2] = happy


maxHappy = -100

for seating in permutations(people):
     seating = list(seating)
     seating.append(seating[0])
     happy = sum(map(lambda x, y: happiness[x][y] + happiness[y][x], seating[0:len(people)], seating[1:len(people)+1]))
     if happy > maxHappy:
         maxHappy = happy

print('The maximum happiness is ', maxHappy)


maxHappy2 = -100

for seating in permutations(people):
     happy = sum(map(lambda x, y: happiness[x][y] + happiness[y][x], seating[0:len(people)-1], seating[1:len(people)]))
     if happy > maxHappy2:
         maxHappy2 = happy

print('The maximum happiness after seating yourself is ', maxHappy2)

if maxHappy > maxHappy2:
    print("People would be happier if you didn't show up at the party.")

