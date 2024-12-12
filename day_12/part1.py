grid = []
with open("day_12/input.txt") as file:
    for line in file:
        grid.append(list(line.strip()))

def is_in_bounds(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

def flood_fill(grid, visited, i, j, target):
    if not is_in_bounds(grid, i, j):
        return 1, 0
    
    if grid[i][j] != target:
        return 1, 0
    
    if visited[i][j] == 1:
        return 0, 0
    
    visited[i][j] = 1

    p1, a1 = flood_fill(grid, visited, i + 1, j, target)
    p2, a2 = flood_fill(grid, visited, i, j + 1, target)
    p3, a3 = flood_fill(grid, visited, i - 1, j, target)
    p4, a4 = flood_fill(grid, visited, i, j - 1, target)

    return p1 + p2 + p3 + p4, a1 + a2 + a3 + a4 + 1


visited = [[0] * len(grid[0]) for _ in range(len(grid))]
result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if visited[i][j] == 0:
            perimiter, area = flood_fill(grid, visited, i, j, grid[i][j])
            result += perimiter * area

print(result)