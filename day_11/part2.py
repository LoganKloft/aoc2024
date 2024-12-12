stones = None
with open("day_11/input.txt") as file:
    stones = list(map(int, file.readline().strip().split()))

def count_stones(stone, num_blinks):
    stones_1 = dict()
    stones_2 = dict()

    dict_read = stones_1
    dict_write = stones_2

    stones_1[stone] = 1
    for _ in range(num_blinks):
        dict_write.clear()
        for key, value in dict_read.items():
            if key == 0:
                new_key = key + 1
                if new_key not in dict_write:
                    dict_write[new_key] = value
                else:
                    dict_write[new_key] += value
                continue

            key_str = str(key)
            key_str_len = len(key_str)
            if key_str_len % 2 == 0:
                new_key_1 = int(key_str[:key_str_len//2])
                new_key_2 = int(key_str[key_str_len//2:])

                if new_key_1 not in dict_write:
                    dict_write[new_key_1] = value
                else:
                    dict_write[new_key_1] += value
                
                if new_key_2 not in dict_write:
                    dict_write[new_key_2] = value
                else:
                    dict_write[new_key_2] += value
                continue
            
            new_key = key * 2024
            if new_key not in dict_write:
                dict_write[new_key] = value
            else:
                dict_write[new_key] += value
        
        dict_read, dict_write = dict_write, dict_read
        
    return sum(dict_read.values())

result = 0
for stone in stones:
    result += count_stones(stone, 75)

print(result)