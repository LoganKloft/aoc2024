rules = dict()
manuals = []

with open("input.txt") as file:
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

result = 0
for manual in manuals:
    seen = set()
    bad_page = False
    for page in manual:
        if page in rules:
            rule = rules[page]
            for rule_page in rule:
                if rule_page in seen:
                    bad_page = True
                    break

        seen.add(page)
            
        if bad_page:
            break
    
    if not bad_page:
        result += manual[len(manual) // 2]

print(result)