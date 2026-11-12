
def findPalindromes(m, n):
    result = []

    for num in range(m, n + 1):
        if str(num) == str(num)[::-1]:
            result.append(num)

    return result


# Example 1
m = 10
n = 50
print(findPalindromes(m, n))

# Example 2
m = 100
n = 150
print(findPalindromes(m, n))

# Example 3
m = 1
n = 9
print(findPalindromes(m, n))
