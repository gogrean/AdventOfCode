tape_message = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

sues = dict()

f = open('sues.dat', 'r')

for line in f.readlines():
    info = line.replace(": ", " ").replace(", ", " ").split()
    for i in range(2, len(info), 2):
        sues.setdefault(info[1], dict())[info[i]] = int(info[i+1])

right_sue = sues.copy()

for item in tape_message.keys():
    for sue in sues.keys():
        if sue in right_sue.keys():
            if item in right_sue[sue].keys() and tape_message[item] != right_sue[sue][item]:
                del right_sue[sue]

sue = list(right_sue.keys())[0]

print("The right Sue in number %s." % sue)


################


right_sue = sues.copy()

for item in tape_message.keys():
    for sue in sues.keys():
        if sue in right_sue.keys():
            if item in right_sue[sue].keys() and (item == "cats" or item == "trees"):
                if tape_message[item] >= right_sue[sue][item]:
                    del right_sue[sue]
            elif item in right_sue[sue].keys() and (item == "pomeranians" or item == "goldfish"):
                if tape_message[item] <= right_sue[sue][item]:
                    del right_sue[sue]
            elif item in right_sue[sue].keys() and tape_message[item] != right_sue[sue][item]:
                del right_sue[sue]

sue = list(right_sue.keys())[0]

print("The right Sue in number %s." % sue)
