import re
from random import shuffle
import sys


def find_medicine(medicine, step):
    shuffle(conversion_pairs)

    if medicine in medicines:
        return None
    medicines.add(medicine)

    if medicine == 'e':
        print('The minimum number of steps is: {} steps'.format(step))
        sys.exit()

    made_replacements = False
    for pair in conversion_pairs:
        idx = [m.start() for m in re.finditer(pair[1], medicine)]
        for ix in idx:
            index, length = ix, len(pair[1])
            previous_mol = medicine[:index] + pair[0] + medicine[index+length:]
            find_medicine(previous_mol, step + 1)
            made_replacements = True

    if not made_replacements:
        if medicine != 'e':
            sys.exit()
        print('The minimum number of steps is: {} steps'.format(step))
    return None


medicine = open('calibration.txt', 'r').read().strip()
conversions = open('molecules.txt', 'r').readlines()

conversion_pairs = []

for conversion in conversions:
    conversion = conversion.strip()
    mol_in, mol_out = conversion.split(" => ")
    conversion_pairs.append((mol_in, mol_out))
    
medicines = set()

find_medicine(medicine, 0)
