
def mergeTriplets(triplets, target):
    result = [0, 0, 0]

    for triplet in triplets:

        # Ignore triplets that exceed the target
        if (triplet[0] > target[0] or
            triplet[1] > target[1] or
            triplet[2] > target[2]):
            continue

        # Update maximum values
        for i in range(3):
            result[i] = max(result[i], triplet[i])

    return result == target


# Example 1
triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target = [2, 7, 5]
print(mergeTriplets(triplets, target))

# Example 2
triplets = [[3, 4, 5], [4, 5, 6]]
target = [3, 2, 5]
print(mergeTriplets(triplets, target))

# Example 3
triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
target = [5, 5, 5]
print(mergeTriplets(triplets, target))
