grid = []
moves = ""

with open("day_15/input.txt") as file:
    reading_grid = True
    for line in file:
        if line.isspace():
            reading_grid = False

        if reading_grid:
            grid.append(list(line.strip()))
        else:
            moves += line.strip()

def get_robot_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return i, j
    return -1, -1

robot_row, robot_col = get_robot_position(grid)

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
    
    while grid[i][j] != '#' and grid[i][j] != '.':
        i, j = i + direction[0], j + direction[1]

    if (grid[i][j] == '#'):
        continue
    
    while grid[i][j] != '@':
        grid[i][j] = grid[i - direction[0]][j - direction[1]]
        i, j = i - direction[0], j - direction[1]
    
    grid[i][j] = '.'
    robot_row, robot_col = i + direction[0], j + direction[1]

result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            result += 100 * i + j

print(result)