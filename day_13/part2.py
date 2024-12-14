a_buttons = []
b_buttons = []
prizes = []

def button_extract_x(line):
    line = line.split()
    line = line[2].split('+')
    return int(line[1][:-1])

def button_extract_y(line):
    line = line.split()
    line = line[3].split('+')
    return int(line[1])

def prize_extract_x(line):
    line = line.split()
    line = line[1].split('=')
    return int(line[1][:-1])

def prize_extract_y(line):
    line = line.split()
    line = line[2].split('=')
    return int(line[1])

with open("day_13\input.txt") as file:
    read_a_line = True
    read_b_line = False
    read_prize_line = False
    read_blank_line = False

    for line in file:
        line = line.strip()
        if read_a_line:
            button_x = button_extract_x(line)
            button_y = button_extract_y(line)
            a_buttons.append((button_x, button_y))
            read_a_line = False
            read_b_line = True
        
        elif read_b_line:
            button_x = button_extract_x(line)
            button_y = button_extract_y(line)
            b_buttons.append((button_x, button_y))
            read_b_line = False
            read_prize_line = True

        elif read_prize_line:
            prize_x = prize_extract_x(line) + 10000000000000 
            prize_y = prize_extract_y(line) + 10000000000000
            prizes.append((prize_x, prize_y))
            read_prize_line = False
            read_blank_line = True

        elif read_blank_line:
            read_blank_line = False
            read_a_line = True

result = 0
button_a_token_cost = 3
button_b_token_cost = 1
for machine_idx in range(len(prizes)):
    x1 = a_buttons[machine_idx][0]
    x2 = b_buttons[machine_idx][0]
    x3 = prizes[machine_idx][0]

    y1 = a_buttons[machine_idx][1]
    y2 = b_buttons[machine_idx][1]
    y3 = prizes[machine_idx][1]

    n2 = (y1*x3 - y3*x1) / (y1*x2 - y2*x1)
    n1 = (x3 - n2*x2) / x1
    if n1.is_integer() and n2.is_integer():
        result += button_a_token_cost * n1 + button_b_token_cost * n2

print(result)