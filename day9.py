#beginner level
arr = [10, 20, 10, 30, 20]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            print("Duplicate:", arr[i])

#medium level
arr = [10, 20, 10, 30, 20, 40]

duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate elements:", duplicates)