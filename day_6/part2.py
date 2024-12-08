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
    if index_in_bounds(grid, row, col):
        return grid[row][col] in '#'
    return False

def insert_barrier(grid, row, col):
    if index_in_bounds(grid, row, col):
        grid[row][col] = '#'

def remove_barrier(grid, row, col):
    if index_in_bounds(grid, row, col):
        grid[row][col] = '.'

def check_cycle(grid, row, col, directions, direction_idx):
    seen = set()

    while index_in_bounds(grid, row, col):
        if (row, col, directions[direction_idx]) in seen:
            return True
        
        if is_barrier(grid, row, col):
            row -= directions[direction_idx][0]
            col -= directions[direction_idx][1]
            direction_idx = (direction_idx + 1) % len(directions)
        else:
            seen.add((row, col, directions[direction_idx]))
            row += directions[direction_idx][0]
            col += directions[direction_idx][1]

    return False

def run_simulation(grid, start_row, start_col):
    row, col = start_row, start_col
    result = 0

    barriers_placed = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_idx = 0
    while index_in_bounds(grid, row, col):
        if is_barrier(grid, row, col):
            row -= directions[direction_idx][0]
            col -= directions[direction_idx][1]
            direction_idx = (direction_idx + 1) % len(directions)

        else:
            barrier_row_idx = row + directions[direction_idx][0]
            barrier_col_idx = col + directions[direction_idx][1]

            if not is_barrier(grid, barrier_row_idx, barrier_col_idx):
                insert_barrier(grid, barrier_row_idx, barrier_col_idx)
                if check_cycle(grid, start_row, start_col, directions, 0):
                    if (barrier_row_idx, barrier_col_idx) not in barriers_placed:
                        result += 1
                        barriers_placed.add((barrier_row_idx, barrier_col_idx))
                remove_barrier(grid, barrier_row_idx, barrier_col_idx)
            
            row += directions[direction_idx][0]
            col += directions[direction_idx][1]
    
    return result

print(run_simulation(grid, start_row, start_col))