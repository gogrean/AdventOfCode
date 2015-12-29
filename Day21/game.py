from itertools import combinations

def winner_calculator(player_stats, boss_stats):
    boss_loss = max(1, player_stats['damage'] - boss_stats['armor']) 
    player_loss = max(1, boss_stats['damage'] - player_stats['armor'])
    player_points = player_stats['hit']
    boss_points = boss_stats['hit']
    while True:
        boss_points -= boss_loss
        if boss_points <= 0:
            return 'player'
        player_points -= player_loss
        if player_points <= 0:
            return 'boss'

boss_stats = {
        'hit': 100,
        'damage': 8,
        'armor': 2
}

weapons = {
        'dagger': {'cost': 8, 'damage': 4},
        'shortsword': {'cost': 10, 'damage': 5},
        'warhammer': {'cost': 25, 'damage': 6},
        'longsword': {'cost': 40, 'damage': 7},
        'greataxe': {'cost': 74, 'damage': 8}
}

armors = {
        'none': {'cost': 0, 'armor': 0},
        'leather': {'cost': 13, 'armor': 1},
        'chainmail': {'cost': 31, 'armor': 2},
        'splintmail': {'cost': 53, 'armor': 3},
        'bandedmail': {'cost': 75, 'armor': 4},
        'platemail': {'cost': 102, 'armor': 5}
}

rings = {
        'none': {'cost': 0, 'damage': 0, 'armor': 0},
        'damage +1': {'cost': 25, 'damage': 1, 'armor': 0},
        'damage +2': {'cost': 50, 'damage': 2, 'armor': 0},
        'damage +3': {'cost': 100, 'damage': 3, 'armor': 0},
        'defense +1': {'cost': 20, 'damage': 0, 'armor': 1},
        'defense +2': {'cost': 40, 'damage': 0, 'armor': 2},
        'defense +3': {'cost': 80, 'damage': 0, 'armor': 3}
}

ring_combinations = list(combinations(rings.keys(),2))
ring_combinations.append(('none', 'none'))

min_gold = None

for weapon in weapons.keys():
    weapon_gold = weapons[weapon]['cost']
    weapon_damage = weapons[weapon]['damage']
    for armor in armors.keys():
        armor_gold = armors[armor]['cost']
        armor_armor = armors[armor]['armor']
        for ring_combo in ring_combinations:
            ring_gold = rings[ring_combo[0]]['cost'] + rings[ring_combo[1]]['cost']
            gold = weapon_gold + armor_gold + ring_gold
            ring_damage = rings[ring_combo[0]]['damage'] \
                    + rings[ring_combo[1]]['damage']
            ring_armor = rings[ring_combo[0]]['armor'] \
                    + rings[ring_combo[1]]['armor']
            player_damage = weapon_damage + ring_damage
            player_armor = armor_armor + ring_armor
            player_stats = {
                'hit': 100,
                'damage': player_damage,
                'armor': player_armor
            }
            winner = winner_calculator(player_stats, boss_stats)
            if winner == 'player':
                if not min_gold or gold < min_gold:
                    min_gold = gold


print('The minimum gold you can pay to win is ', min_gold)
