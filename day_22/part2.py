numbers = []
with open("day_22/input.txt") as file:
    for line in file:
        numbers.append(int(line.strip()))

def get_secret_number(number):
    # step 1
    intermediate = number * 64
    number = intermediate ^ number
    number = number % 16777216

    # step 2
    intermediate = number // 32
    number = number ^ intermediate
    number = number % 16777216

    # step 3
    intermediate = number * 2048
    number = number ^ intermediate
    number = number % 16777216

    return number

iterations = 2000
prices = [[] for _ in range(len(numbers))]
changes = [[] for _ in range(len(numbers))]
for i in range(len(numbers)):
    number = numbers[i]
    prices[i].append(number % 10)
    changes[i].append(0)
    for _ in range(iterations):
     number = get_secret_number(number)
     prices[i].append(number % 10)
     changes[i].append(prices[i][-1] - prices[i][-2])

sequences = [dict() for _ in range(len(numbers))]
for i in range(len(numbers)):
    for j in range(1, iterations - 3):
        sequence = (changes[i][j], changes[i][j + 1], changes[i][j + 2], changes[i][j + 3])
        
        if sequence not in sequences[i]:
            sequences[i][sequence] = prices[i][j + 3]

# 1842 * 1999 * 1842 = 6782535036
max_sum = 0
for i in range(len(numbers)):
    for key in sequences[i].keys():
        curr_sum = 0
        for j in range(len(numbers)):
            if key in sequences[j]:
                curr_sum += sequences[j][key]
        if curr_sum > max_sum:
            max_sum = curr_sum
    print(i)
             
print(max_sum)