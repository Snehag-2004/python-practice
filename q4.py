
def decodeWays(s):
    result = []

    def backtrack(index, current):
        if index == len(s):
            result.append(current)
            return

        # Check single digit
        if s[index] != '0':
            num = int(s[index])
            letter = chr(64 + num)
            backtrack(index + 1, current + letter)

        # Check two digits
        if index + 1 < len(s):
            num = int(s[index:index + 2])

            if 10 <= num <= 26:
                letter = chr(64 + num)
                backtrack(index + 2, current + letter)

    backtrack(0, "")

    print("Total Ways:", len(result))

    if result:
        print("Decoded Strings:")
        for word in result:
            print(word)
    else:
        print("Decoded Strings: None")


# Example 1
s = "12"
decodeWays(s)

# Example 2
s = "226"
decodeWays(s)

# Example 3
s = "11106"
decodeWays(s)

# Example 4
s = "06"
decodeWays(s)
