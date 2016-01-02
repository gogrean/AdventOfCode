import numpy as np
from math import ceil
from itertools import combinations

weights = np.loadtxt('package_weights.txt', dtype=int)

total_weight = np.sum(weights)
compartment_weight = total_weight/4.

qe_min = np.prod(weights)

for n_items_c1 in range(1, ceil(len(weights)/4)):
    for items_c1 in combinations(weights, n_items_c1):
        if np.sum(items_c1) == compartment_weight:
            remaining_weights = [x for x in weights if x not in items_c1]
            for n_items_c2 in range(n_items_c1, ceil(len(remaining_weights)/3)):
                for items_c2 in combinations(remaining_weights, n_items_c2):
                    used_weights = np.concatenate((items_c1, items_c2))
                    if np.sum(items_c2) == compartment_weight:
                        remaining_weights = [x for x in weights if x not in used_weights]
                        for n_items_c3 in range(n_items_c2, ceil(len(remaining_weights)/2)):
                            for items_c3 in combinations(remaining_weights, n_items_c3):
                                used_weights = np.concatenate((items_c1, items_c2, items_c3))
                                if np.sum(items_c3) == compartment_weight:
                                    items_c4 = [x for x in weights if x not in used_weights]
                                    if len(items_c4) < n_items_c1:
                                        continue
                                    else:
                                        qe = np.prod(items_c1)
                                        if qe < qe_min:
                                            qe_min = qe

print(qe_min)
