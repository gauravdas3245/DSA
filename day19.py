numbers = [10, -5, 20, -2, 0, -15, 8]
count = 0

for num in numbers:
    if num < 0:
        count += 1

print("Negative numbers:", count)