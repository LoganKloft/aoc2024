patterns = []
designs = []

max_design_length = 0
with open("day_19/input.txt") as file:
    # read pattern line
    patterns = file.readline().strip().split(', ')

    # read blank line
    file.readline().strip()

    for line in file:
        designs.append(line.strip())
        max_design_length = max(max_design_length, len(designs[-1]))

def count_match_design(design, patterns):
    count = [0] * len(design)

    for pattern in patterns:
        if len(pattern) > len(design):
            continue

        if pattern == design[0:len(pattern)]:
            count[len(pattern) - 1] += 1

    for i in range(len(design)):
        if count[i] == 0:
            continue

        for pattern in patterns:
            if len(pattern) > len(design) - i - 1:
                continue
            
            if pattern == design[i + 1 : i + 1 + len(pattern)]:
                count[i + len(pattern)] += count[i]

    return count[-1]

result = 0
for design in designs:
    result += count_match_design(design, patterns)
print(result)