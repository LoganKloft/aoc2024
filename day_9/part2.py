disk_layout = []
with open("day_9\input.txt") as file:
    line = file.readline().strip()

    # initialize disk_layout
    disk_layout.append([0, int(line[0]), False, 0])
    for i in range(1, len(line)):
        idx, size = disk_layout[-1][0], disk_layout[-1][1]
        if i % 2 == 1:
            disk_layout.append([idx + size, int(line[i]), True])
        else:
            disk_layout.append([idx + size, int(line[i]), False, i // 2])

def compact_disk(disk_layout, idx):
    shortened_by = 0
    if idx + 1 < len(disk_layout):
        if disk_layout[idx + 1][2] and disk_layout[idx][2]:
            disk_layout[idx][1] += disk_layout[idx + 1][1]
            disk_layout.pop(idx + 1)
    
    if idx - 1 >= 0:
        if disk_layout[idx - 1][2] and disk_layout[idx][2]:
            disk_layout[idx - 1][1] += disk_layout[idx][1]
            disk_layout.pop(idx)
            shortened_by = 1
    
    return shortened_by

right_idx = len(disk_layout) - 1
result = 0
while right_idx >= 0:
    left_idx = 0
    while left_idx < right_idx:
        if disk_layout[left_idx][2] and disk_layout[left_idx][1] > disk_layout[right_idx][1]:
            right_copy = disk_layout[right_idx].copy()
            right_copy[0] = disk_layout[left_idx][0]
            disk_layout[left_idx][0] = right_copy[0] + right_copy[1]
            disk_layout[left_idx][1] -= right_copy[1]
            disk_layout[right_idx][2] = True
            disk_layout[right_idx].pop(3)
            right_idx -= compact_disk(disk_layout, right_idx)
            disk_layout.insert(left_idx, right_copy)
            break

        elif disk_layout[left_idx][2] and disk_layout[left_idx][1] == disk_layout[right_idx][1]:
            disk_layout[left_idx][2] = False
            disk_layout[left_idx].append(disk_layout[right_idx][3])
            disk_layout[right_idx].pop(3)
            disk_layout[right_idx][2] = True
            right_idx -= compact_disk(disk_layout, right_idx)
            break
        else:
            left_idx += 1
    
    if left_idx == right_idx:
        right_idx -= 1

    while right_idx >= 0 and disk_layout[right_idx][2]:
        right_idx -= 1

result = 0
for i in range(len(disk_layout)):
    if disk_layout[i][2] == False:
        position = disk_layout[i][0]
        size = disk_layout[i][1]
        for j in range(position, position + size):
            result += j * disk_layout[i][3]

print(result)