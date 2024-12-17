maze = []
with open("day_16/input.txt") as file:
    for line in file:
        maze.append(line.strip())

visited = dict()
def find_least_cost(maze, visited, i, j, cost, direction):
    frontier = [(i, j, cost, direction)]
    directions = [(0,1),(-1,0),(0,-1),(1,0)]
    
    while frontier:
        i, j, cost, direction = frontier.pop()

        if maze[i][j] == '#':
            continue
        
        if (i, j, direction) in visited and visited[(i, j, direction)] <= cost:
            continue
        visited[(i, j, direction)] = cost

        if maze[i][j] == 'E':
            continue
        
        # continue straight
        frontier.append((i + directions[direction][0], j + directions[direction][1], cost + 1, direction))

        # turn right
        tmp_direction = direction
        if direction == 0:
            tmp_direction = 3
        else:
            tmp_direction = direction - 1
        frontier.append((i + directions[tmp_direction][0], j + directions[tmp_direction][1], cost + 1001, tmp_direction))

        # turn left
        tmp_direction = (direction + 1) % 4
        frontier.append((i + directions[tmp_direction][0], j + directions[tmp_direction][1], cost + 1001, tmp_direction))

def find_end_position(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'E':
                return (i, j)
    return (-1, -1)

def find_start_position(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                return (i, j)
    return (-1, -1)

start_position = find_start_position(maze)

find_least_cost(maze, visited, start_position[0], start_position[1], 0, 0)

result = -1
end_position = find_end_position(maze)

for key, value in visited.items():
    if (key[0], key[1]) == end_position:
        if result == -1:
            result = value
        else:
            result = min(result, value) 

print(result)