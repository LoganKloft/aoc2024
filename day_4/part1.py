def in_bounds(grid, row_idx, col_idx):
    rows = len(grid)
    cols = len(grid[0])
    return row_idx >= 0 and col_idx >= 0 and row_idx < rows and col_idx < cols 

def check_direction(grid, row_idx, col_idx, direction, word):
    word_idx = 0
    while word_idx < len(word):
        if not in_bounds(grid, row_idx, col_idx):
            return 0
        
        if grid[row_idx][col_idx] != word[word_idx]:
            return 0
        
        row_idx += direction[0]
        col_idx += direction[1]
        word_idx += 1

    return 1

# parse file
grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(list(line.strip()))

# run algorithm on grid
result = 0
directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
rows = len(grid)
cols = len(grid[0])
for row_idx in range(rows):
    for col_idx in range(cols):
        for direction in directions:
            result += check_direction(grid, row_idx, col_idx, direction, "XMAS")

print(result)