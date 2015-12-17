import re
import string

def trueHex(x):
    isHex = False
    true_x = [i for i in x if i in string.hexdigits]
    if x == true_x:
        isHex = True
    return isHex


f = open('santas_list.txt', 'r')
lines = f.readlines()

delChar = 0

for line in lines:
    line = line.strip()
    # Ignore start/end quotation marks. Otherwise issues with strings such as 'uxi\\"'
    line = line[1:len(line)-1]
    # Add start/end quotation marks to sum of deleted characters.
    delChar += 2
    if line.count("\\\\") or line.count("\\\""):
        # Add backslashes and escaped quotation marks to the sum. 
        delChar += line.count("\\\\") + line.count("\\\"")
    # Add hex to sum. First check it's actually hex.
    hexCharIndex = [m.start() for m in re.finditer(r"\\x", line)]
    if hexCharIndex:
        for i in hexCharIndex:
            if trueHex([line[i+2], line[i+3]]):
                delChar += 3

print("The difference is ", delChar)


addChar = 0

for line in lines:
    line = line.strip()
    line = line[1:len(line)-1]
    # Account for start/end quotation marks, plus the additional quotation marks to make new string.
    addChar += 4
    if line.count("\\\\") or line.count("\\\""):
        addChar += 2*(line.count("\\\\") + line.count("\\\""))
    hexCharIndex = [m.start() for m in re.finditer(r"\\x", line)]
    if hexCharIndex:
        for i in hexCharIndex:
            if trueHex([line[i+2], line[i+3]]):
                addChar += 1

print("The number of additional characters is ", addChar)


            
