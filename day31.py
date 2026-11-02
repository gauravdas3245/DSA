
def max_subarray_sum(numbers):
    current_sum = numbers[0]
    max_sum = numbers[0]

    for num in numbers[1:]:
        current_sum = max(num, current_sum + num)

        max_sum = max(max_sum, current_sum)

    return max_sum


numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_subarray_sum(numbers))
