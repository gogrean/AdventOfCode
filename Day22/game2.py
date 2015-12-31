import heapq
from copy import deepcopy

player_armor = 0
boss_damage = 9

initial = {
    'Player Hit Points': 50,
    'Boss Hit Points': 58,
    'Player Mana': 500,
    'Shield Turns': 0,
    'Poison Turns': 0,
    'Recharge Turns': 0
}

spells = {
    'Magic Missile': {'cost': 53, 'damage': 4},
    'Drain': {'cost': 73, 'damage': 2, 'heal': 2},
    'Shield': {'cost': 113, 'timer': 6, 'armor': 7},
    'Poison': {'cost': 173, 'timer': 6, 'damage': 3},
    'Recharge': {'cost': 229, 'timer': 5, 'mana': 101}
}

states = [(0, 0, initial)]

def boss_turn(state):
    timer_effects(state)
    if state[2]['Boss Hit Points'] > 0:
        if state[2]['Shield Turns'] > 0:
            damage = max(1, boss_damage - spells['Shield']['armor'])
        else:
            damage = boss_damage
        state[2]['Player Hit Points'] -= damage 

def timer_effects(state):
    if state[2]['Shield Turns'] > 0:
        state[2]['Shield Turns'] -= 1
    if state[2]['Poison Turns'] > 0:
        state[2]['Boss Hit Points'] -= spells['Poison']['damage']
        state[2]['Poison Turns'] -= 1
    if state[2]['Recharge Turns'] > 0:
        state[2]['Player Mana'] += spells['Recharge']['mana']
        state[2]['Recharge Turns'] -= 1

state_serial = 1
def do_magic(state, spell):
    global state_serial

    state = deepcopy(state)
    timer_effects(state)  
 
    if state[2]['Player Mana'] < spells[spell]['cost']:
        return None

    state = (state[0] + spells[spell]['cost'], state_serial, state[2])
    state_serial += 1

    state[2]['Player Mana'] -= spells[spell]['cost']
    if spell == 'Magic Missile':
        state[2]['Boss Hit Points'] -= spells['Magic Missile']['damage']
    if spell == 'Drain':
        state[2]['Boss Hit Points'] -= spells['Drain']['damage']
        state[2]['Player Hit Points'] += spells['Drain']['heal']
    if spell == 'Shield':
        if state[2]['Shield Turns'] > 0:
            return None
        state[2]['Shield Turns'] = spells['Shield']['timer']
    if spell == 'Poison':
        if state[2]['Poison Turns'] > 0:
            return None
        state[2]['Poison Turns'] = spells['Poison']['timer'] 
    if spell == 'Recharge':
        if state[2]['Recharge Turns'] > 0:
            return None
        state[2]['Recharge Turns'] = spells['Recharge']['timer']
    return state

def next_states(state):
    new_states = []
    state[2]['Player Hit Points'] -= 1
    if state[2]['Player Hit Points'] <= 0:
        return new_states
    for spell in spells:
        new_state = do_magic(state, spell)
        if new_state is not None:
            boss_turn(new_state)
            new_states.append(new_state)
    return new_states

index = 0
while True:
    mana_used, serial, state = heapq.heappop(states)
    index += 1
    if state['Boss Hit Points'] <= 0:
        print('The minimum amount of mana used is ', mana_used)
        break
    elif state['Player Hit Points'] <= 0:
        continue
    else:
       for new_state in next_states( (mana_used, serial, state) ):
           heapq.heappush(states, new_state) 
