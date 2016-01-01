
commands = open('instructions.txt', 'r').readlines()

reg = {
    'a': 1,
    'b': 0
}

i = 0

while True:
    if i >= len(commands):
        break
    command = commands[i].split()
    if command[0] == 'hlf':
        reg[command[1]] /= 2
    if command[0] == 'inc':
        reg[command[1]] += 1
    if command[0] == 'tpl':
        reg[command[1]] *= 3
    if command[0] == 'jmp':
        i += int(command[1])
        continue
    if command[0] == 'jie':
        if reg[command[1].strip(',')] % 2 == 0:
            i += int(command[2])
            continue
    if command[0] == 'jio':
        if reg[command[1].strip(',')] == 1:
            i += int(command[2])
            continue
    i += 1

print('The registers are: \n', reg)
