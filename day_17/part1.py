A = 0
B = 0
C = 0
pointer = 0
program = []

def adv(operand):
    global A, B, C, pointer
    A = int(A / (2**decode_combo_operand(operand)))
    pointer += 2

def bxl(operand):
    global A, B, C, pointer
    B = B ^ operand
    pointer += 2

def bst(operand):
    global A, B, C, pointer
    B = decode_combo_operand(operand) % 8
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
    global A, B, C, pointer
    print(decode_combo_operand(operand) % 8, end=',')
    pointer += 2

def bdv(operand):
    global A, B, C, pointer
    B = int(A / 2**decode_combo_operand(operand))
    pointer += 2

def cdv(operand):
    global A, B, C, pointer
    C = int(A / 2**decode_combo_operand(operand))
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
    program = list(map(int,line.split()[-1].split(',')))

while pointer < len(program):
    operator = decode_operator(program[pointer])
    operand = program[pointer + 1]

    operator(operand)