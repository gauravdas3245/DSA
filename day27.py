
def merge_alternately(a, b):
    result = []
    limit = min(len(a), len(b))

    for i in range(limit):
        result.append(a[i])
        result.append(b[i])

    result.extend(a[limit:])
    result.extend(b[limit:])

    return result


a = [1, 2, 3]
b = [10, 20, 30, 40]

print(merge_alternately(a, b))
