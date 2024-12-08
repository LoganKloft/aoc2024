def is_increasing(levels):
    for i in range(len(levels) - 1):
        if int(levels[i]) >= int(levels[i + 1]):
            return False, i
        if abs(int(levels[i]) - int(levels[i + 1])) > 3:
            return False, i
    return True, -1

def is_decreasing(levels):
    for i in range(len(levels) - 1):
        if int(levels[i]) <= int(levels[i + 1]):
            return False, i
        if abs(int(levels[i]) - int(levels[i + 1])) > 3:
            return False, i
    return True, -1

def is_safe(levels):
    res1, idx1 = is_increasing(levels)
    res2, idx2 = is_decreasing(levels)

    if res1 or res2:
        return 1

    cpy1_1 = levels.copy()
    cpy1_2 = levels.copy()
    cpy1_1.pop(idx1)
    cpy1_2.pop(idx1 + 1)

    cpy2_1 = levels.copy()
    cpy2_2 = levels.copy()
    cpy2_1.pop(idx2)
    cpy2_2.pop(idx2 + 1)

    if is_increasing(cpy1_1)[0] or is_decreasing(cpy1_1)[0]:
        return 1
    if is_increasing(cpy1_2)[0] or is_decreasing(cpy1_2)[0]:
        return 1
    if is_increasing(cpy2_1)[0] or is_decreasing(cpy2_1)[0]:
        return 1
    if is_increasing(cpy2_2)[0] or is_decreasing(cpy2_2)[0]:
        return 1

    return 0

result = 0
with open("day_2/input.txt") as file:
    for line in file:
        levels = line.strip().split()
        result += is_safe(levels)

print(result)