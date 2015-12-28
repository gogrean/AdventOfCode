from itertools import combinations

containers = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, \
    7, 18, 43, 10, 47, 36, 24, 22, 40]

eggnog_vol = 150

n_combs = 0

min_comb = len(containers)
n_min_comb = 0

for n_containers in range(2,len(containers)):
    for comb in combinations(containers, n_containers):
        if sum(comb) == eggnog_vol:
            n_combs += 1
            if n_containers == min_comb:
                n_min_comb += 1
            if n_containers < min_comb:
                min_comb = n_containers
                n_min_comb = 1

print("There are %i ways to store the eggnog." % n_combs)
print("There are %i ways to store the eggnog in the least possible number of containers (%i)." % (n_min_comb, min_comb) )

#############




