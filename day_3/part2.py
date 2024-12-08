import re

def get_x_y(mul_str):
    x,y = re.findall(r"\d{1,3}", mul_str)
    return int(x), int(y)

result = 0
with open("day_3/input.txt") as file:
    do = True
    for line in file:
        matches = re.findall(r"(don't\(\))|(do\(\))|(mul\(\d{1,3},\d{1,3}\))", line.strip())
        for match in matches:
            if match[0]:
                do = False
            elif match[1]:
                do = True
            elif do:
                x, y = get_x_y(match[2])
                result += x * y

print(result)