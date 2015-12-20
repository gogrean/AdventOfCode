import operator
import functools

def score(ingredients, tsps):
    points = []
    props = list(ingredients.values())
    for i in range(4):
        points.append(tsps[0]*props[0][i] + \
                tsps[1]*props[1][i] + tsps[2]*props[2][i] + \
                tsps[3]*props[3][i])
    calories = tsps[0]*props[0][4] + tsps[1]*props[1][4] + \
                tsps[2]*props[2][4] + tsps[3]*props[3][4]
    neg = [i for i in points if i < 0]
    if neg:
        points = [0] 
    return functools.reduce(operator.mul, points, 1), calories
    

f = open('ingredients.txt', 'r')
info = f.readlines()

ingredients = {}

for line in info:
    ingredient = line.split(": ")[0]
    properties = line.split(": ")[1].split(", ")
    values = [int(properties[i].split()[1]) for i in range(len(properties))]
    ingredients[ingredient] = values


n_tsp = 100
max_cookie_score = 0

for i in range(n_tsp+1):
    for j in range(n_tsp-i+1):
        for k in range(n_tsp-i-j+1):
            for l in range(n_tsp-i-j-k+1):
                tsps = [i, j, k, l]
                cookie_score, calories = score(ingredients, tsps)
                if cookie_score > max_cookie_score and calories == 500:
                    max_cookie_score = cookie_score

print("The maximum cookie score is: %i" % max_cookie_score)

