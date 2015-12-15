from inputs import *

f = open('manual.txt', 'r')
instructions = f.readlines()

op = {
    'NOT': lambda x: ~ x,
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'XOR': lambda x, y: x ^ y,
    'LSHIFT': lambda x, y: x << y,
    'RSHIFT': lambda x, y: x >> y
}

def solve_wires(instructions, op, overwrite=None):
    if not overwrite:
        solved = {}
    else:
        solved = overwrite   # In case the user overwrites (part of) the manual.
    # While not all signals calculated...
    while len(solved) != len(instructions) :
        for instruction in instructions:
            in_out = instruction.split("->")
            in_out[1] = in_out[1].strip()
            # If signal for the wire already calculated,
            # then don't waste time re-calculating it.
            if in_out[1] in solved:
                continue
            items = [x.strip() for x in in_out[0].split(" ") if x]
            if len(items) == 1:
                solved[in_out[1]] = direct_input(items[0], solved)
            elif len(items) == 2:
                solved[in_out[1]] = indirect_single_input(items, op, solved)
            elif len(items) == 3:
                solved[in_out[1]] = indirect_double_input(items, op, solved)
            elif len(items) < 1 or len(items) > 3:
                print("Instruction was not understood: ", instruction)
                break
            solved = {k: v for k, v in solved.items() if v != None}
    return(solved)

solved = solve_wires(instructions, op)
print("The signal for wire 'a' is: ", solved['a'])    

solved = solve_wires(instructions, op, overwrite = {'b': 46065})
print("After overwritting 'b', the signal for wire 'a' is: ", solved['a'])
    
 
