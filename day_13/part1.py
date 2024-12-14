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
            prize_x = prize_extract_x(line)
            prize_y = prize_extract_y(line)
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
    min_token_cost = 100 * button_a_token_cost + 100 * button_b_token_cost
    min_cost_updated = False
    for a_presses in range(101): # a presses
        for b_presses in range(101): # b presses
            x = a_buttons[machine_idx][0] * a_presses + b_buttons[machine_idx][0] * b_presses
            y = a_buttons[machine_idx][1] * a_presses + b_buttons[machine_idx][1] * b_presses

            if x == prizes[machine_idx][0] and y == prizes[machine_idx][1]:
                if a_presses * button_a_token_cost + b_presses * button_b_token_cost < min_token_cost:
                    min_token_cost = a_presses * button_a_token_cost + b_presses * button_b_token_cost
                    min_cost_updated = True

    if min_cost_updated:
        result += min_token_cost

print(result)