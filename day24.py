numbers = [4, 5, 1, 2, 1, 4, 5]

for num in numbers:
    if numbers.count(num) == 1:
        print("First non-repeating number:", num)
        break
else:
    print("No non-repeating number found")