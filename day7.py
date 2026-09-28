arr = [10, 5, 20, 8, 15]

largest = arr[0]
second = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] > second and arr[i] != largest:
        second = arr[i]

print("Second largest:", second)