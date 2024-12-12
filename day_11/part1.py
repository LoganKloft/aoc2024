stones = None
with open("day_11/input.txt") as file:
    stones = list(map(int, file.readline().strip().split()))

def count_stones(stone):
    stones = [stone]
    max_blinks = 25
    
    for _ in range(max_blinks):
        stones_size = len(stones)
        for i in range(stones_size):
            if stones[i] == 0:
                stones[i] = 1
                continue
            
            stone_str = str(stones[i])
            stone_len = len(stone_str)
            if stone_len % 2 == 0:
                stones.append(int(stone_str[:stone_len // 2]))
                stones[i] = int(stone_str[stone_len//2:])
                continue

            stones[i] *= 2024
    
    return len(stones)
            
result = 0
for stone in stones:
    result += count_stones(stone)

print(result)