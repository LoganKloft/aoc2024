maze = []
with open("day_16/input.txt") as file:
    for line in file:
        maze.append(list(line.strip()))

visited = dict()
def find_least_cost(maze, visited, i, j, cost, direction):
    frontier = [(i, j, cost, direction)]
    directions = [(0,1),(-1,0),(0,-1),(1,0)]
    
    while frontier:
        i, j, cost, direction = frontier.pop()

        if maze[i][j] == '#':
            continue
        
        if (i, j) in visited:
            if visited[(i, j)][direction] != -1 and visited[(i, j)][direction] <= cost:
                continue
        else:
            visited[(i, j)] = [-1] * 4
        
        visited[(i, j)][direction] = cost

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

end_position = find_end_position(maze)
result = max(visited[end_position])
for i in range(4):
    if visited[end_position][i] != -1 and visited[end_position][i] < result:
        result = visited[end_position][i]

back_track_positions = []
for i in range(4):
    if visited[end_position][i] == result:
        back_track_positions.append((end_position[0], end_position[1], result, i))

def back_track(maze, visited, back_track_positions):
    frontier = back_track_positions
    directions = [(0,1),(-1,0),(0,-1),(1,0)]
    while frontier:
        i, j, cost, direction = frontier.pop()
        maze[i][j] = 'O'

        # did i come from same direction?
        i_prev = i - directions[direction][0]
        j_prev = j - directions[direction][1]
        cost_prev = cost - 1
        direction_prev = direction
        if (i_prev, j_prev) in visited and visited[(i_prev, j_prev)][direction_prev] == cost_prev:
            frontier.append((i_prev, j_prev, cost_prev, direction_prev))

        # did i come from left?
        i_prev = i - directions[direction][0]
        j_prev = j - directions[direction][1]
        cost_prev = cost - 1001
        direction_prev = direction - 1
        if direction_prev < 0:
            direction_prev = 3
        if (i_prev, j_prev) in visited and visited[(i_prev, j_prev)][direction_prev] == cost_prev:
            frontier.append((i_prev, j_prev, cost_prev, direction_prev))

        # did i come from right?
        i_prev = i - directions[direction][0]
        j_prev = j - directions[direction][1]
        cost_prev = cost - 1001
        direction_prev = (direction + 1) % 4
        if (i_prev, j_prev) in visited and visited[(i_prev, j_prev)][direction_prev] == cost_prev:
            frontier.append((i_prev, j_prev, cost_prev, direction_prev))

back_track(maze, visited, back_track_positions)

def count_o(maze):
    count = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'O':
                count += 1
    return count 

print(count_o(maze))