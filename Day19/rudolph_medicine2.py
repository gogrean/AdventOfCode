import re
from random import shuffle
import sys


def find_medicine(medicine, step):
    shuffle(conversion_pairs)

    for pair in conversion_pairs:
        idx = [m.start() for m in re.finditer(pair[1], medicine)]
        for ix in idx:
            index, length = ix, len(pair[1])
            previous_mol = medicine[:index] + pair[0] + medicine[index+length:]
            return find_medicine(previous_mol, step + 1)

    print('Found {}. The minimum number of steps is: {} steps'.format(medicine, step))
    return medicine


medicine = open('calibration.txt', 'r').read().strip()
conversions = open('molecules.txt', 'r').readlines()

conversion_pairs = []

for conversion in conversions:
    conversion = conversion.strip()
    mol_in, mol_out = conversion.split(" => ")
    conversion_pairs.append((mol_in, mol_out))
    
while True:
    medi = find_medicine(medicine, 0)
    if medi == 'e':
        break


