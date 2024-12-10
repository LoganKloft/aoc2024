disk_map = None
with open("day_9\input.txt") as file:
    disk_map = file.readline().strip()

result = 0
position = 0
left_file_idx = 0
right_file_idx = len(disk_map) - 1
right_block_count = int(disk_map[right_file_idx])
free_space_idx = 1
free_space = int(disk_map[free_space_idx])

while left_file_idx < right_file_idx:
    if left_file_idx < free_space_idx:
        for _ in range(int(disk_map[left_file_idx])):
            result += position * (left_file_idx // 2)
            position += 1
        left_file_idx += 2
    else:
        while free_space > 0 and right_block_count > 0:
            result += position * (right_file_idx // 2)
            position += 1
            free_space -= 1
            right_block_count -= 1
        
        if free_space == 0:
            free_space_idx += 2
            free_space = int(disk_map[free_space_idx])
        
        if right_block_count == 0:
            right_file_idx -= 2
            right_block_count = int(disk_map[right_file_idx])

while right_block_count > 0:
    result += position * (right_file_idx // 2)
    position += 1
    right_block_count -= 1

print(result)