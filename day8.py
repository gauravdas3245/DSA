arr = [0, 1, 0, 3, 12]

result = []

for i in range(len(arr)):
    if arr[i] != 0:
        result.append(arr[i])

while len(result) < len(arr):
    result.append(0)

print(result)