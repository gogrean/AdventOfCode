import re
from math import floor

cal_molecule = open('calibration.txt', 'r').read().strip()

conversions = open('molecules.txt', 'r').readlines()

molecules = set()

for conversion in conversions:
    conversion = conversion.strip("\n")
    mol_in, mol_out = conversion.split(" => ")
    idx = [m.start() for m in re.finditer(mol_in, cal_molecule)]
    for i in idx:
        molecule = cal_molecule[:i] + mol_out + cal_molecule[i+len(mol_in):]
        molecules.add(molecule)

print("The number of molecules created is ", len(molecules))


