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

def calculate_antinode_coords(antenna_1_coord, antenna_2_coord, bounds, antinodes):
    x_difference = abs(antenna_1_coord[0] - antenna_2_coord[0])
    y_difference = abs(antenna_1_coord[1] - antenna_2_coord[1])

    antinode_1_change = [x_difference,y_difference]
    antinode_2_change = [x_difference,y_difference]
    if antenna_1_coord[0] < antenna_2_coord[0]:
        antinode_1_change[0] *= -1
    else:
        antinode_2_change[0] *= -1
    
    if antenna_1_coord[1] < antenna_2_coord[1]:
        antinode_1_change[1] *= -1
    else:
        antinode_2_change[1] *= -1
    
    num_antinodes = 0
    antinode_1_coord = [antenna_1_coord[0] + antinode_1_change[0], antenna_1_coord[1] + antinode_1_change[1]]
    antinode_2_coord = [antenna_2_coord[0] + antinode_2_change[0], antenna_2_coord[1] + antinode_2_change[1]]

    while is_in_bounds(antinode_1_coord, bounds):
        antinodes.add(tuple(antinode_1_coord))
        antinode_1_coord[0] += antinode_1_change[0]
        antinode_1_coord[1] += antinode_1_change[1]

    while is_in_bounds(antinode_2_coord, bounds):
        antinodes.add(tuple(antinode_2_coord))
        antinode_2_coord[0] += antinode_2_change[0]
        antinode_2_coord[1] += antinode_2_change[1]
    
    antinodes.add(antenna_1_coord)
    antinodes.add(antenna_2_coord)

def is_in_bounds(coord, bounds):
    return coord[0] >= 0 and coord[1] >= 0 and coord[0] < bounds[0] and coord[1] < bounds[1]

bounds = [len(grid), len(grid[0])]
for key, value in antennas.items():
    num_antennas = len(value)
    for antenna_1_idx in range(num_antennas - 1):
        for antenna_2_idx in range(antenna_1_idx + 1, num_antennas):
            calculate_antinode_coords(value[antenna_1_idx], value[antenna_2_idx], bounds, antinodes)

print(len(antinodes))