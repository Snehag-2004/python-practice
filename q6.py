
def reverseInteger(x):
    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
        digit = x % 10
        x = x // 10

        if result > (2**31 - 1) // 10:
            return 0

        if result == (2**31 - 1) // 10:
            if digit > (8 if sign == -1 else 7):
                return 0

        result = result * 10 + digit

    return sign * result


# Example 1
print(reverseInteger(123))

# Example 2
print(reverseInteger(-123))

# Example 3
print(reverseInteger(120))
