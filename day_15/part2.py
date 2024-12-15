grid = []
moves = ""

with open("day_15/input.txt") as file:
    reading_grid = True
    for line in file:
        if line.isspace():
            reading_grid = False

        if reading_grid:
            grid_entry = []
            for c in line.strip():
                if c == '.':
                    grid_entry.append('.')
                    grid_entry.append('.')
                elif c == '@':
                    grid_entry.append('@')
                    grid_entry.append('.')
                elif c == 'O':
                    grid_entry.append('[')
                    grid_entry.append(']')
                elif c == '#':
                    grid_entry.append('#')
                    grid_entry.append('#')
            grid.append(grid_entry)
        else:
            moves += line.strip()

def get_robot_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return i, j
    return -1, -1

robot_row, robot_col = get_robot_position(grid)

def move_box_left_right(grid, i, j, direction):
    next_i, next_j = i, j
    while grid[next_i][next_j] != '#' and grid[next_i][next_j] != '.':
        next_i, next_j = next_i + direction[0], next_j + direction[1]
    
    if grid[next_i][next_j] == '#':
        return
    
    while grid[next_i][next_j] != '@':
        grid[next_i][next_j] = grid[next_i - direction[0]][next_j - direction[1]]
        next_i, next_j = next_i - direction[0], next_j - direction[1]
    
    grid[next_i][next_j] = '.'
    
def box_can_move_up_down(grid, i, j, direction):
    if grid[i][j] == ']':
        j -= 1

    next_i, next_j = i + direction[0], j + direction[1]

    if grid[next_i][next_j] == '#':
        return False

    if grid[next_i][next_j + 1] == '#':
        return False

    res_1 = True
    if grid[next_i][next_j] in '[]':
        res_1 = box_can_move_up_down(grid, next_i, next_j, direction)
    
    res_2 = True
    if grid[next_i][next_j + 1] == '[':
        res_2 = box_can_move_up_down(grid, next_i, next_j + 1, direction)
    
    if res_1 and res_2:
        return True
    return False
        

def move_box_up_down(grid, i, j, direction):
    if grid[i][j] == ']':
        j -= 1

    next_i, next_j = i + direction[0], j + direction[1]

    if grid[next_i][next_j] == '#':
        return

    if grid[next_i][next_j + 1] == '#':
        return

    if grid[next_i][next_j] in '[]':
        move_box_up_down(grid, next_i, next_j, direction)
    
    if grid[next_i][next_j + 1] == '[':
        move_box_up_down(grid, next_i, next_j + 1, direction)
    
    if grid[next_i][next_j] == '.' and grid[next_i][next_j + 1] == '.':
        grid[i][j] = '.'
        grid[i][j + 1] = '.'
        grid[next_i][next_j] = '['
        grid[next_i][next_j + 1] = ']'

for move in moves:
    direction = (0, 0)
    if move == '<':
        direction = (0, -1)
    elif move == '>':
        direction = (0, 1)
    elif move == '^':
        direction = (-1, 0)
    elif move == 'v':
        direction = (1, 0)
    
    i, j = robot_row + direction[0], robot_col + direction[1]

    if grid[i][j] == '#':
        continue
    if grid[i][j] == '.':
        grid[i][j] = '@'
        grid[robot_row][robot_col] = '.'
        robot_row, robot_col = i, j
        continue
    
    if move in '<>':
        move_box_left_right(grid, i, j, direction)

    elif move in 'v^':
        if box_can_move_up_down(grid, i, j, direction):
            move_box_up_down(grid, i, j, direction)
    
    if grid[i][j] == '.' or grid[i][j] == '@':
        grid[i][j] = '@'
        grid[robot_row][robot_col] = '.'
        robot_row, robot_col = i, j

result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '[':
            result += 100 * i + j

print(result)