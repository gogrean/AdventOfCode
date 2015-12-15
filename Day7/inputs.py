def direct_input(x, solved):
    if x.isdigit():
        y = int(x)
    elif x.islower() and x in solved:
        y = int(solved[x])
    else:
        y = None
    return y

def indirect_single_input(x, op, solved):
    action = op[x[0]]
    in1 = direct_input(x[1], solved)
    if in1 != None:
        y = action(in1)
    else:
        y = None
    return y

def indirect_double_input(x, op, solved):
    action = op[x[1]]
    in1 = direct_input(x[0], solved)
    in2 = direct_input(x[2], solved)
    if in1 != None and in2 != None:
        y = action(in1, in2)
    else:
        y = None
    return y

