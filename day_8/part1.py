antennas = dict()
grid = []
antinodes = set()

with open("day_8\input.txt") as file:
    for line in file:
        grid.append(list(line.strip()))

def find_antenna_in_grid(grid, antennas):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != '.':
                antenna_symbol = grid[row][col]
                if antenna_symbol not in antennas:
                    antennas[antenna_symbol] = list()
                
                antennas[antenna_symbol].append((row, col))

find_antenna_in_grid(grid, antennas)

def calculate_antinode_coords(antenna_1_coord, antenna_2_coord):
    x_difference = abs(antenna_1_coord[0] - antenna_2_coord[0])
    y_difference = abs(antenna_1_coord[1] - antenna_2_coord[1])

    antinode_1_coord = list(antenna_1_coord)
    antinode_2_coord = list(antenna_2_coord)
    if antenna_1_coord[0] < antenna_2_coord[0]:
        antinode_1_coord[0] -= x_difference
        antinode_2_coord[0] += x_difference
    else:
        antinode_1_coord[0] += x_difference
        antinode_2_coord[0] -= x_difference
    
    if antenna_1_coord[1] < antenna_2_coord[1]:
        antinode_1_coord[1] -= y_difference
        antinode_2_coord[1] += y_difference
    else:
        antinode_1_coord[1] += y_difference
        antinode_2_coord[1] -= y_difference
    
    return tuple(antinode_1_coord), tuple(antinode_2_coord)

def is_in_bounds(grid, x, y):
    return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])

for key, value in antennas.items():
    num_antennas = len(value)
    for antenna_1_idx in range(num_antennas - 1):
        for antenna_2_idx in range(antenna_1_idx + 1, num_antennas):
            antinode_1_coord, antinode_2_coord = calculate_antinode_coords(value[antenna_1_idx], value[antenna_2_idx])
            if is_in_bounds(grid, antinode_1_coord[0], antinode_1_coord[1]):
                antinodes.add(antinode_1_coord)
            if is_in_bounds(grid, antinode_2_coord[0], antinode_2_coord[1]):
                antinodes.add(antinode_2_coord)

print(len(antinodes))