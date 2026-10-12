a = [1, 4, 7, 10]
b = [2, 3, 8, 9]

merged = []
i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

merged.extend(a[i:])
merged.extend(b[j:])

print("Merged list:", merged)