import numpy as np

f = open('naughty_strings.txt', 'r')
strings = f.readlines()

bad_strings = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']

good_strings = []

for string in strings:
    if not [i for i in bad_strings if i in string]:
        if len([j for j in string if j in vowels]) >= 3:
           if len([k for k in np.arange(len(string)-1) if string[k] == string[k+1]]) > 0:
               good_strings.append(string)

print('There are ', len(good_strings), ' nice strings.')

########

good_strings = []

for string in strings:
    string = string.strip()
    pairs = {}
    overlap = False
    for i in range(len(string)):
        pairs.setdefault(string[i:i+2], 0)
        if i != 0 and overlap == False and string[i:i+2] == string[i-1:i+1]:
            overlap = True
        else:
            pairs[string[i:i+2]] += 1
        overlap = False
    if [i for i in pairs if pairs[i] > 1]:
        if len([k for k in np.arange(len(string)-2) if string[k] == string[k+2]]) > 0:
            good_strings.append(string)

print('After Santa changed his mind about the rules, there are ', len(good_strings), ' good strings.')

 
