numbers = [4, -2, 7, -5, 1, -8, 3]

left = []
right = []

for num in numbers:
    if num < 0:
        left.append(num)
    else:
        right.append(num)

result = left + right

print("Result:", result)