import re
import json

f = open("json_input.txt", 'r')
text = f.read()

numbers = [int(num) for num in re.findall(r'-?\d+', text)]
numbers_sum = sum(numbers)

print("The sum of all the numbers in the file is: ", numbers_sum)


def deleteReds(x):
    if 'red' in x.values():
        x.clear()
    return x

objects = json.loads(text, object_hook=deleteReds)

numbers = [int(num) for num in re.findall(r'-?\d+', str(objects))]
numbers_sum = sum(numbers)

print("The sum of all the numbers in the file after removing 'red' is: ", numbers_sum)

