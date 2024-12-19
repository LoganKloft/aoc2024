rows = 71
cols = 71
grid = [['.'] * cols for _ in range(rows)]

num_to_plot = 1024
num_plotted = 0
with open("day_18/input.txt") as file:
    for line in file:
        col_idx, row_idx = line.strip().split(',')
        col_idx, row_idx = int(col_idx), int(row_idx)

        if num_plotted != num_to_plot:
            grid[row_idx][col_idx] = '#'
            num_plotted += 1

def is_in_bounds(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

def get_min_path_length(grid, i, j, length):
    visited = dict()
    frontier = [(i, j, length)]
    while frontier:
        i, j, length = frontier.pop()

        if not is_in_bounds(grid, i, j):
            continue
        
        if grid[i][j] == '#':
            continue

        if (i, j) in visited and visited[(i, j)] <= length:
            continue

        visited[(i, j)] = length
        frontier.append((i, j + 1, length + 1))
        frontier.append((i, j - 1, length + 1))
        frontier.append((i + 1, j, length + 1))
        frontier.append((i - 1, j, length + 1))

    return visited[(len(grid) - 1, len(grid[0]) - 1)]

print(get_min_path_length(grid, 0, 0, 0))