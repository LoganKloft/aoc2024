rules = dict()
manuals = []

def check_manual(manual, rules):
    seen = set()
    for page_idx in range(len(manual)):
        page = manual[page_idx]
        if page in rules:
            rule = rules[page]
            for rule_page in rule:
                if rule_page in seen:
                    return page_idx

        seen.add(page)

    return -1

with open("day_5/input.txt") as file:
    for line in file:
        if "|" in line:
            x, y = line.strip().split('|')
            x, y = int(x), int(y)
            if x in rules:
                rules[x].add(y)
            else:
                rules[x] = set()
                rules[x].add(y)
        elif line.isspace():
            continue
        else:
            manuals.append(list(map(int, line.strip().split(','))))

bad_manuals = []
for manual in manuals:
    res = check_manual(manual, rules)
    
    if res != -1:
        bad_manuals.append(manual)
 
result = 0
for manual in bad_manuals:
    while True:
        res = check_manual(manual, rules)
        if res == -1:
            result += manual[len(manual) // 2]
            break
        else:
            manual[res], manual[res - 1] = manual[res - 1], manual[res]

print(result)