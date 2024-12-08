left_nums = []
right_nums = []

with open("day_1/input.txt") as file:
    for line in file:
        left, right = line.strip().split()
        left_nums.append(int(left))
        right_nums.append(int(right))

right_freq = {}
result = 0

for num in right_nums:
    right_freq[num] = right_freq.get(num, 0) + 1

for i in range(len(left_nums)):
    result = result + left_nums[i] * right_freq.get(left_nums[i], 0)

print(result)