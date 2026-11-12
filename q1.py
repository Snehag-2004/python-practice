
def singleNumber(nums):
    result = 0

    for num in nums:
        result = result ^ num

    return result


# Example 1
nums = [2, 2, 1]
print(singleNumber(nums))

# Example 2
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))

# Example 3
nums = [1]
print(singleNumber(nums))
