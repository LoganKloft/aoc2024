grid = []
grid_score = []
with open("day_10/input.txt") as file:
    for line in file:
        grid.append(line.strip())
        grid_score.append([0] * len(grid[0]))

def is_in_bounds(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

def get_trailhead_score(grid, i, j, grid_score):
    frontier = [(i, j, -1)]
    while frontier:
        i, j, k = frontier.pop()
        
        if is_in_bounds(grid, i, j):
            grid_value = int(grid[i][j])
            if grid_value == k + 1:
                grid_score[i][j] += 1
                if grid_value < 9:
                    frontier.append((i + 1, j, grid_value))
                    frontier.append((i, j + 1, grid_value))
                    frontier.append((i - 1, j, grid_value))
                    frontier.append((i, j - 1, grid_value))

result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '0':
            get_trailhead_score(grid, i, j, grid_score)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '9':
            result += grid_score[i][j]

print(result)