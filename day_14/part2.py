import numpy as np
from PIL import Image
# parameters
rows = 103
cols = 101
seconds = 10000

# structures
grid = [[0] * cols for _ in range(rows)]
positions = []
velocities = []

def get_position(line):
    line = line.split()
    line = line[0].split('=')
    line = line[1].split(',')
    return [int(line[0]), int(line[1])]

def get_velocity(line):
    line = line.split()
    line = line[1].split('=')
    line = line[1].split(',')
    return (int(line[0]), int(line[1]))

with open("day_14/input.txt") as file:
    for line in file:
        positions.append(get_position(line.strip()))
        velocities.append(get_velocity(line.strip()))
        grid[positions[-1][1]][positions[-1][0]] += 1

def is_in_bounds(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

def has_neighbor(grid, i, j):
    directions = [(1,0),(1,1),(-1,0),(-1,-1),(0,-1),(0,1),(1,-1),(-1,1)]
    for direction in directions:
        a = i + direction[0]
        b = j + direction[1]
        if is_in_bounds(grid, a, b) and grid[a][b] > 0:
            return True
    return False

def count_neighbors(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if has_neighbor(grid, i, j):
                count += 1
    return count

def largest_row_count(grid):
    max_row_count = 0
    for i in range(len(grid)):
        row_count = 0
        for j in range(len(grid[0])):
            if (grid[i][j]) > 0:
                row_count += 1
        
        if row_count > max_row_count:
            max_row_count = row_count
    return max_row_count

def largest_col_count(grid):
    max_col_count = 0
    for i in range(len(grid[0])):
        col_count = 0
        for j in range(len(grid)):
            if (grid[j][i]) > 0:
                col_count += 1
        
        if col_count > max_col_count:
            max_col_count = col_count
    return max_col_count

def create_and_save_image(grid, second):
    array = np.zeros((len(grid), len(grid[0]),3), dtype=np.uint8)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] > 0):
                array[i][j][0] = 255
    
    img = Image.fromarray(array)
    img.save("tree_" + str(second) + ".png")

max_count = 0
max_row_count = 0
time = 0
row_count_time_idx = 0
for time_idx in range(seconds):
    for robot_idx in range(len(positions)):
        grid[positions[robot_idx][1]][positions[robot_idx][0]] -= 1
        positions[robot_idx][1] = (positions[robot_idx][1] + velocities[robot_idx][1]) % rows
        positions[robot_idx][0] = (positions[robot_idx][0] + velocities[robot_idx][0]) % cols
        grid[positions[robot_idx][1]][positions[robot_idx][0]] += 1

    # count = count_neighbors(grid)
    # if count > max_count:
    #     max_count = count
    #     time = time_idx + 1
    #     print(time, max_count)

    #     for i in range(len(grid)):
    #         print(grid[i])
    #     input("press any key to continue...")

    row_count = largest_row_count(grid)
    col_count = largest_col_count(grid)
    if row_count + col_count > max_row_count:
        max_row_count = row_count + col_count
        row_count_time_idx = time_idx + 1
        print(row_count_time_idx, max_row_count)
        create_and_save_image(grid, time_idx + 1)

print(time, max_count)