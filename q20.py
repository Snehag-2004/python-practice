
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    result = []

    def backtrack(start, path):
        if start == len(s):
            result.append(" ".join(path))
            return

        for end in range(start + 1, len(s) + 1):
            word = s[start:end]

            if word in wordSet:
                backtrack(end, path + [word])

    backtrack(0, [])

    if result:
        print("Can Segment: True")
        print("Segmentations:")
        for sentence in result:
            print(sentence)
    else:
        print("Can Segment: False")
        print("Segmentations: None")


# Example 1
s = "AmritaMysuru"
wordDict = ["Amrita", "Rita", "Mysuru"]
wordBreak(s, wordDict)

# Example 2
s = "applepenapple"
wordDict = ["apple", "pen"]
wordBreak(s, wordDict)

# Example 3
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
wordBreak(s, wordDict)

# Example 4
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
wordBreak(s, wordDict)
