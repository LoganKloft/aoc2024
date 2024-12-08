grid = []
with open("day_6/input.txt") as file:
    for line in file:
        grid.append(list(line.strip()))

def get_start_location(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '^':
                return row, col
    return -1, -1

start_row, start_col = get_start_location(grid)

def index_in_bounds(grid, row, col):
    return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])

def is_barrier(grid, row, col):
    return grid[row][col] in '#'

def mark_grid(grid, row, col):
    grid[row][col] = 'X'

def is_marked(grid, row, col):
    return grid[row][col] == 'X'

def run_simulation(grid, start_row, start_col):
    row, col = start_row, start_col

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_idx = 0
    while index_in_bounds(grid, row, col):
        if is_barrier(grid, row, col):
            row -= directions[direction_idx][0]
            col -= directions[direction_idx][1]
            direction_idx = (direction_idx + 1) % len(directions)

        else:
            mark_grid(grid, row, col)
            row += directions[direction_idx][0]
            col += directions[direction_idx][1]

run_simulation(grid, start_row, start_col)

def count_marks(grid):
    result = 0
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if is_marked(grid, row, col):
                result += 1
    return result

print(count_marks(grid))