import numpy as np

present_goal = 34e6
house = 0
houses = np.arange(1e6) + 1

#while True:
#    house += 1
#
#    sliced = houses[0:house]
#    multiples = sliced[house % sliced == 0]
#    presents = np.sum(multiples) * 10 
#
#    if house % 1000 == 0:
#        print(house, presents)
#
#    if presents >= present_goal:
#        print("The house number is %i" % house)
#        break
    

########

house = 0
houses = np.arange(1e6) + 1

while True:
    house += 1

    sliced = houses[(house-1)//50:house]
    multiples = sliced[house % sliced == 0]
    presents = np.sum(multiples) * 11

    if house % 1000 == 0:
        print(house, presents)

    if presents >= present_goal:
        print("The house number is %i" % house)
        break


