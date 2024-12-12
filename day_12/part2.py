grid = []
with open("day_12/input.txt") as file:
    for line in file:
        grid.append(list(line.strip()))

def is_in_bounds(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

def flood_fill(grid, visited, i, j, target, walked, direction):
    if not is_in_bounds(grid, i, j) or grid[i][j] != target:
        if (i, j, direction) not in walked:
            if direction == "left":
                j += 1
                while is_in_bounds(grid, i, j) and grid[i][j] == target:
                    if is_in_bounds(grid, i, j - 1) and grid[i][j - 1] == target:
                        break
                    walked.add((i, j - 1, direction))
                    i += 1
                i -= 1
                while is_in_bounds(grid, i, j) and grid[i][j] == target:
                    if is_in_bounds(grid, i, j - 1) and grid[i][j - 1] == target:
                        break
                    walked.add((i, j - 1, direction))
                    i -= 1
            elif direction == "right":
                j -= 1
                while is_in_bounds(grid, i, j) and grid[i][j] == target:
                    if is_in_bounds(grid, i, j + 1) and grid[i][j + 1] == target:
                        break
                    walked.add((i, j + 1, direction))
                    i += 1
                i -= 1
                while is_in_bounds(grid, i, j) and grid[i][j] == target:
                    if is_in_bounds(grid, i, j + 1) and grid[i][j + 1] == target:
                        break
                    walked.add((i, j + 1, direction))
                    i -= 1                
            elif direction == "up":
                i += 1
                while is_in_bounds(grid, i, j) and grid[i][j] == target:
                    if is_in_bounds(grid, i - 1, j) and grid[i - 1][j] == target:
                        break
                    walked.add((i - 1, j, direction))
                    j += 1
                j -= 1
                while is_in_bounds(grid, i, j) and grid[i][j] == target:
                    if is_in_bounds(grid, i - 1, j) and grid[i - 1][j] == target:
                        break
                    walked.add((i - 1, j, direction))
                    j -= 1
            elif direction == "down":
                i -= 1
                while is_in_bounds(grid, i, j) and grid[i][j] == target:
                    if is_in_bounds(grid, i + 1, j) and grid[i + 1][j] == target:
                        break
                    walked.add((i + 1, j, direction))
                    j += 1
                j -= 1
                while is_in_bounds(grid, i, j) and grid[i][j] == target:
                    if is_in_bounds(grid, i + 1, j) and grid[i + 1][j] == target:
                        break
                    walked.add((i + 1, j, direction))
                    j -= 1
            return 1, 0, 1
        return 1, 0, 0
    
    if visited[i][j] == 1:
        return 0, 0, 0
    
    visited[i][j] = 1

    p1, a1, s1 = flood_fill(grid, visited, i + 1, j, target, walked, "down")
    p2, a2, s2 = flood_fill(grid, visited, i, j + 1, target, walked, "right")
    p3, a3, s3 = flood_fill(grid, visited, i - 1, j, target, walked, "up")
    p4, a4, s4 = flood_fill(grid, visited, i, j - 1, target, walked, "left")

    return p1 + p2 + p3 + p4, a1 + a2 + a3 + a4 + 1, s1 + s2 + s3 + s4

visited = [[0] * len(grid[0]) for _ in range(len(grid))]
result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if visited[i][j] == 0:
            walked = set()
            perimiter, area, sides = flood_fill(grid, visited, i, j, grid[i][j], walked, "")
            result += sides * area

print(result)