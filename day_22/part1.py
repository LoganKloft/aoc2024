numbers = []
with open("day_22/input.txt") as file:
    for line in file:
        numbers.append(int(line.strip()))

def get_secret_number(number, iterations):
    for _ in range(iterations):
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

result = 0
for number in numbers:
    result += get_secret_number(number, 2000)

print(result)