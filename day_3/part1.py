import re

def get_x_y(mul_str):
    x,y = re.findall(r"\d{1,3}", mul_str)
    return int(x), int(y)

result = 0
with open("day_3/input.txt") as file:
    for line in file:
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line.strip())
        for match in matches:
            x, y = get_x_y(match)
            result += x * y

print(result)