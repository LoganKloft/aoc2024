test_values = []
test_numbers = []

with open("input.txt") as file:
    for line in file:
        value, numbers = line.strip().split(':')
        numbers = numbers.split()

        test_values.append(int(value))
        test_numbers.append(list(map(int, numbers)))

def apply_operations(target_value, current_value, numbers, idx):
    if idx >= len(numbers):
        return current_value
    
    if current_value > target_value:
        return current_value

    val1 = apply_operations(
        target_value, 
        current_value + numbers[idx], 
        numbers, 
        idx + 1
    )

    if val1 == target_value:
        return val1
    
    val2 = apply_operations(
        target_value,
        current_value * numbers[idx],
        numbers,
        idx + 1
    )

    if val2 == target_value:
        return val2

    val3 = apply_operations(
        target_value,
        int(str(current_value) + str(numbers[idx])),
        numbers,
        idx + 1
    )

    return val3


result = 0
for i in range(len(test_values)):
    res = apply_operations(
        test_values[i], 
        test_numbers[i][0], 
        test_numbers[i], 
        1
    )

    if res == test_values[i]:
        result += test_values[i]

print(result)