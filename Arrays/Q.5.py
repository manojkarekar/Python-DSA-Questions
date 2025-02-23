#Find the missing number in an array (1 to N)


def find_missing_sum(arr):
    n = len(arr)+1 # Since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example usage
arr = [1, 2, 4, 5, 6]
print(find_missing_sum(arr))  # Output: 3
