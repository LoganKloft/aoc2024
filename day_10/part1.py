grid = []
with open("day_10/input.txt") as file:
    for line in file:
        grid.append(line.strip())

def is_in_bounds(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

def get_trailhead_score(grid, i, j):
    visited = set()
    frontier = [(i, j, -1)]

    score = 0
    while frontier:
        i, j, k = frontier.pop()

        if (i, j, k) in visited:
            continue
        
        if is_in_bounds(grid, i, j):
            grid_value = int(grid[i][j])
            if grid_value == k + 1:
                if grid_value == 9:
                    score += 1

                else:
                    frontier.append((i + 1, j, grid_value))
                    frontier.append((i, j + 1, grid_value))
                    frontier.append((i - 1, j, grid_value))
                    frontier.append((i, j - 1, grid_value))

        
        visited.add((i, j, k))

    return score

result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '0':
            result += get_trailhead_score(grid, i, j)

print(result)