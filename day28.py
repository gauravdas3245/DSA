
def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    low = 0
    high = rows * cols - 1

    while low <= high:
        mid = (low + high) // 2

        row = mid // cols
        col = mid % cols

        if matrix[row][col] == target:
            return (row, col)

        elif matrix[row][col] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

print(search_matrix(matrix, 9))
