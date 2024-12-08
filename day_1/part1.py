left_nums = []
right_nums = []

with open("day_1/input.txt") as file:
    for line in file:
        left, right = line.strip().split()
        left_nums.append(int(left))
        right_nums.append(int(right))

left_nums.sort()
right_nums.sort()

result = 0

for i in range(len(left_nums)):
    result = result + abs(left_nums[i] - right_nums[i])

print(result)