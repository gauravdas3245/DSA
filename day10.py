arr = [1, 2, 4, 5]

n = 5
total = n * (n + 1) // 2

sum_arr = 0
for num in arr:
    sum_arr += num

missing = total - sum_arr

print("Missing number:", missing)