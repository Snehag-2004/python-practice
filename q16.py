
def separateLettersDigits(s):
    letters = ""
    digits = ""

    for ch in s:
        if ch.isalpha():
            letters += ch
        elif ch.isdigit():
            digits += ch

    return [letters, digits]


# Example 1
s = "a1b2c3d4"
print(separateLettersDigits(s))

# Example 2
s = "x9y8z7"
print(separateLettersDigits(s))

# Example 3
s = "12345"
print(separateLettersDigits(s))

# Example 4
s = "abcdef"
print(separateLettersDigits(s))
