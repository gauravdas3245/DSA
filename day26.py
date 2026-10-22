numbers = [2, 4, 6, 3, 5, 7, 9, 1]

longest = 1
current = 1

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current += 1
    else:
        current = 1

    if current > longest:
        longest = current

print("Longest increasing run:", longest)