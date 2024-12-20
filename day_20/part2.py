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

def race_with_cheats(racetrack, race_route, i, j):
    distances = dict()
    count = 0
    for route in race_route:
        i, j = route

        for route in race_route:
            a, b = route

            cheat_distance = abs(i - a) + abs(j - b)
            distance_saved = racetrack[a][b] - racetrack[i][j] - cheat_distance
            if cheat_distance <= 20 and distance_saved >= 100:
                count += 1
                if distance_saved not in distances:
                    distances[distance_saved] = 0
                distances[distance_saved] += 1

    return count

i, j = get_start_position(racetrack)
race(racetrack, race_route, i, j)
print(race_with_cheats(racetrack, race_route, i, j))