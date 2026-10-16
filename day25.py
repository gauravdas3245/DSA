numbers = [10, 15, 23, 30, 42]

for i in range(len(numbers) - 1):
    difference = numbers[i + 1] - numbers[i]
    print(numbers[i], "to", numbers[i + 1], ":", difference)