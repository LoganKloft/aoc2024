def in_bounds(grid, row_idx, col_idx):
    rows = len(grid)
    cols = len(grid[0])
    return row_idx >= 0 and col_idx >= 0 and row_idx < rows and col_idx < cols 

def check_pattern(grid, row_idx, col_idx, pattern):   
    for pattern_row_idx in range(len(pattern)):
        for pattern_col_idx in range(len(pattern[0])):
            if not in_bounds(grid, row_idx + pattern_row_idx, col_idx + pattern_col_idx):
                return 0
            
            if pattern[pattern_row_idx][pattern_col_idx] == '.':
                continue
                
            if grid[row_idx + pattern_row_idx][col_idx + pattern_col_idx] != pattern[pattern_row_idx][pattern_col_idx]:
                return 0
        
    return 1

# parse file
grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(list(line.strip()))


# run algorithm on grid
result = 0
rows = len(grid)
cols = len(grid[0])
patterns = [
    [
        ['M','.','M'],
        ['.','A','.'],
        ['S','.','S']
    ],
    [
        ['M','.','S'],
        ['.','A','.'],
        ['M','.','S']
    ],
    [
        ['S','.','S'],
        ['.','A','.'],
        ['M','.','M']
    ],
    [
        ['S','.','M'],
        ['.','A','.'],
        ['S','.','M']
    ]
]
for row_idx in range(rows):
    for col_idx in range(cols):
        for pattern in patterns:
            result += check_pattern(grid, row_idx, col_idx, pattern)

print(result)