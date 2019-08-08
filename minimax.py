
import random

def Max(sticks, depth, t = 1):
    total = sticks
    coup = 0
    max = -100
    val = -99
    coups = []
    if depth == 0:
        return Rules(sticks)
    else:
        for x in range(1,4):
            sticks = sticks - x
            if sticks > 0:
                val = Min(sticks, depth - 1)
            sticks = total
            if val == max or x == 1 and t == 1:
                coups.append(x)
            if val > max:
                max = val
                coup = x
                if x != 1 and t == 1:
                    coups.clear()
    if t == 1:
        if len(coups) > 1 and t == 1:
            coup = random.choices(coups)[0]
        return str(coup)
    else:
        return max
    


def Min(sticks, depth):
    total = sticks
    min = 100
    val = min
    if depth == 0:
        return Rules(sticks)
    else:
        for x in range(1,4):
            sticks = sticks - x
            if sticks > 0:
                val = Max(sticks, depth - 1, 0)
            sticks = total
            if val < min:
                min = val
    return min

def Rules(sticks):
    if sticks <= 1:
        return -1
    elif sticks > 1 and sticks <= 4:
        return 1
    else:
        return 0