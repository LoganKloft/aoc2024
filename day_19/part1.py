patterns = []
designs = []
with open("day_19/input.txt") as file:
    # read pattern line
    patterns = file.readline().strip().split(', ')

    # read blank line
    file.readline().strip()

    for line in file:
        designs.append(line.strip())

def can_match_design(design, patterns):
    candidates = []
    for pattern in patterns:
        if design.startswith(pattern):
            candidates.append(pattern)

    while candidates:
        candidate = candidates.pop()

        for pattern in patterns:
            towel = candidate + pattern
            if towel == design:
                return True

            if design.startswith(towel):
                candidates.append(towel)

    return False

result = 0
for design in designs:
    if can_match_design(design, patterns):
        result += 1
print(result)