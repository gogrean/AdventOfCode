import numpy as np
import hashlib

key1 = 'iwrupvqb'

start = ''
key2 = 1
while start != '000000':
    s = key1 + str(key2)
    md5 = hashlib.md5(s.encode('utf-8')).hexdigest()
    start = md5[0:6]
    print(key2, ' ', start)
    key2 += 1

print('The smallest number is ', key2-1)


