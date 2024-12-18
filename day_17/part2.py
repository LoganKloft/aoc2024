A = 0
B = 0
C = 0
pointer = 0
program = []
program_str = ''
temp_program_str = ''

def adv(operand):
    global A, B, C, pointer
    operand = decode_combo_operand(operand)
    if operand == None:
        pointer = len(program)
        return
    A = int(A / (2**operand))
    pointer += 2

def bxl(operand):
    global A, B, C, pointer
    B = B ^ operand
    pointer += 2

def bst(operand):
    global A, B, C, pointer
    operand = decode_combo_operand(operand)
    if operand == None:
        pointer = len(program)
        return
    B = operand % 8
    pointer += 2

def jnz(operand):
    global A, B, C, pointer
    if A != 0:
        pointer = operand
    else:
        pointer += 2

def bxc(operand):
    global A, B, C, pointer
    B = B ^ C
    pointer += 2

def out(operand):
    global A, B, C, pointer, temp_program_str
    operand = decode_combo_operand(operand)
    if operand == None:
        pointer = len(program)
        return
    pointer += 2
    temp_program_str += str(operand % 8)

def bdv(operand):
    global A, B, C, pointer
    operand = decode_combo_operand(operand)
    if operand == None:
        pointer = len(program)
        return
    B = int(A / 2**operand)
    pointer += 2

def cdv(operand):
    global A, B, C, pointer
    operand = decode_combo_operand(operand)
    if operand == None:
        pointer = len(program)
        return
    C = int(A / 2**operand)
    pointer += 2

def decode_combo_operand(operand):
    if operand < 4:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    if operand == 7:
        return None

def decode_operator(operator):
    if operator == 0:
        return adv
    if operator == 1:
        return bxl
    if operator == 2:
        return bst
    if operator == 3:
        return jnz
    if operator == 4:
        return bxc
    if operator == 5:
        return out
    if operator == 6:
        return bdv
    if operator == 7:
        return cdv

with open("day_17/input.txt") as file:
    # get A register
    line = file.readline().strip()
    A = int(line.split()[-1])

    # get B register
    line = file.readline().strip()
    B = int(line.split()[-1])

    # get C register
    line = file.readline().strip()
    C = int(line.split()[-1])

    # skip empty line
    line = file.readline()
    
    # get program
    line = file.readline().strip()
    program_str = ''.join(line.split()[-1].split(','))
    program = list(map(int, line.split()[-1].split(',')))

def run_simulation(A_start, B_start, C_start):
    global temp_program_str, pointer, A, B, C
    A = A_start
    B = B_start
    C = C_start
    pointer = 0
    temp_program_str = ''

    while pointer < len(program):
        operator = decode_operator(program[pointer])
        operand = program[pointer + 1]

        operator(operand)

A_start = 0
B_start = B
C_start = C

a_vals = []
for j in range(8):
    run_simulation(j, B_start, C_start)
    if temp_program_str == program_str[-len(temp_program_str):]:
        a_vals.append(j)

min_value = -1
while a_vals:
    A_start = a_vals.pop()
    
    if min_value != -1 and A_start > min_value:
        continue

    for j in range(8):
        cpy = A_start
        cpy = cpy << 3
        cpy += j

        run_simulation(cpy, B_start, C_start)

        if temp_program_str == program_str:
            if min_value == -1:
                min_value = cpy
            else:
                min_value = min(min_value, cpy)

        if temp_program_str == program_str[-len(temp_program_str):]:
            a_vals.append(cpy)

print(min_value)