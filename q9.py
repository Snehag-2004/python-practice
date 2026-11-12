
def findPalindromes(s):
    result = []

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result.append(s[left:right + 1])
            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd length palindromes
        expand(i, i)

        # Even length palindromes
        expand(i, i + 1)

    print("Total Count:", len(result))
    print("Palindromic Substrings:")

    for p in result:
        print(p)


# Example 1
s = "ababa"
findPalindromes(s)

# Example 2
s = "racecar"
findPalindromes(s)

# Example 3
s = "level"
findPalindromes(s)
