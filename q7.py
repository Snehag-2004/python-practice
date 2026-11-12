
def maxConsecutiveZeros(s):
    count = 0
    maximum = 0

    for ch in s:
        if ch == '0':
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0

    return maximum


def generateStrings(L, K):
    strings = []

    def backtrack(s, ones):
        if len(s) == L:
            if ones == K:
                strings.append(s)
            return

        if ones < K:
            backtrack(s + '1', ones + 1)

        if L - len(s) > K - ones:
            backtrack(s + '0', ones)

    backtrack("", 0)

    print("Possible Strings:")

    minZeros = L + 1
    optimal = []

    for s in strings:
        zeros = maxConsecutiveZeros(s)
        print(s, "-> max zeros =", zeros)

        if zeros < minZeros:
            minZeros = zeros
            optimal = [s]
        elif zeros == minZeros:
            optimal.append(s)

    print("Optimal Arrangement(s):", ", ".join(optimal))
    print("Minimum Longest Zero Block:", minZeros)


# Get input
L, K = map(int, input("Enter L and K: ").split())

generateStrings(L, K)

