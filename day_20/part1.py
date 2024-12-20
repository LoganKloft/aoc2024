racetrack = []
race_route = []
with open("day_20/input.txt") as file:
    for line in file:
        racetrack.append(list(line.strip()))

def get_start_position(racetrack):
    for i in range(len(racetrack)):
        for j in range(len(racetrack[i])):
            if racetrack[i][j] == 'S':
                return i, j
    return -1, -1

def race(racetrack, race_route, i, j):
    distance = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while racetrack[i][j] != 'E':
        racetrack[i][j] = distance
        for direction in directions:
            if racetrack[i + direction[0]][j + direction[1]] == '.' or racetrack[i + direction[0]][j + direction[1]] == 'E':
                race_route.append((i, j))
                i += direction[0]
                j += direction[1]
                break
        distance += 1
    racetrack[i][j] = distance
    race_route.append((i, j))
    return distance

def is_in_bounds(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

def race_with_cheats(racetrack, race_route, i, j):
    distances = dict()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for route in race_route:
        i, j = route

        for direction_1 in directions:
            cheat_i = i + direction_1[0]
            cheat_j = j + direction_1[1]

            if racetrack[cheat_i][cheat_j] == '#':
                for direction_2 in directions:
                    cheat_ii = cheat_i + direction_2[0]
                    cheat_jj = cheat_j + direction_2[1]

                    if is_in_bounds(racetrack, cheat_ii, cheat_jj) and racetrack[cheat_ii][cheat_jj] != '#':
                        distance = racetrack[cheat_ii][cheat_jj] - racetrack[i][j] - 2
                        if distance >= 100:
                            if distance not in distances:
                                distances[distance] = 0
                            distances[distance] += 1
    
    return sum(distances.values())

i, j = get_start_position(racetrack)
race(racetrack, race_route, i, j)
print(race_with_cheats(racetrack, race_route, i, j))