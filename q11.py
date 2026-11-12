
def missingNumber(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2

    actual_sum = sum(nums)

    return expected_sum - actual_sum


# Example 1
nums = [3, 0, 1]
print("Missing Number:", missingNumber(nums))

# Example 2
nums = [0, 1]
print("Missing Number:", missingNumber(nums))

# Example 3
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print("Missing Number:", missingNumber(nums))
