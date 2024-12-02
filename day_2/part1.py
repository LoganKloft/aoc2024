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
    if int(levels[0]) > int(levels[1]):
        return is_decreasing(levels)
    if int(levels[0]) < int(levels[1]):
        return is_increasing(levels)    
    return False, 0

result = 0
with open("input.txt") as file:
    for line in file:
        levels = line.strip().split()
        result += is_safe(levels)[0] 

print(result)