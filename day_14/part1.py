positions = []
velocities = []

def get_position(line):
    line = line.split()
    line = line[0].split('=')
    line = line[1].split(',')
    return (int(line[0]), int(line[1]))

def get_velocity(line):
    line = line.split()
    line = line[1].split('=')
    line = line[1].split(',')
    return (int(line[0]), int(line[1]))

with open("day_14/input.txt") as file:
    for line in file:
        positions.append(get_position(line.strip()))
        velocities.append(get_velocity(line.strip()))

# parameters
rows = 103
cols = 101
seconds = 100
grid = [[0] * cols for _ in range(rows)]

for robot_idx in range(len(positions)):
    row = (positions[robot_idx][1] + velocities[robot_idx][1] * seconds) % rows
    col = (positions[robot_idx][0] + velocities[robot_idx][0] * seconds) % cols
    grid[row][col] += 1

result = 0
quad1, quad2, quad3, quad4 = 0, 0, 0, 0
for i in range(0, rows // 2):
    for j in range(0, cols // 2):
        quad1 += grid[i][j]
for i in range(0, rows // 2):
    for j in range(cols - cols // 2, cols):
        quad2 += grid[i][j]
for i in range(rows - rows // 2, rows):
    for j in range(0, cols // 2):
        quad3 += grid[i][j]
for i in range(rows - rows // 2, rows):
    for j in range(cols - cols // 2, cols):
        quad4 += grid[i][j]

print(quad1 * quad2 * quad3 * quad4)