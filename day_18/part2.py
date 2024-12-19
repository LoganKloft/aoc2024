rows = 71
cols = 71
grid = [['.'] * cols for _ in range(rows)]
corruptions = []

num_to_plot = 1024
num_plotted = 0
with open("day_18/input.txt") as file:
    for line in file:
        col_idx, row_idx = line.strip().split(',')
        col_idx, row_idx = int(col_idx), int(row_idx)

        corruptions.append((row_idx, col_idx))

while num_plotted < num_to_plot:
    grid[corruptions[num_plotted][0]][corruptions[num_plotted][1]] = '#'
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

    if (len(grid) - 1, len(grid[0]) - 1) not in visited:
        return True

    return False

def plot(grid, amount, corruptions):
    for i in range(amount):
        grid[corruptions[i][0]][corruptions[i][1]] = '#'

def clear_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = '.'

plot(grid, len(corruptions) - 594, corruptions)
print(get_min_path_length(grid, 0, 0, 0))
clear_grid(grid)
print(corruptions[len(corruptions) - 594 - 1][1], ',', corruptions[len(corruptions) - 594 - 1][0])