
def mergeIntervals(intervals):
    intervals.sort()

    result = []

    for interval in intervals:

        if not result or result[-1][1] < interval[0]:
            result.append(interval)

        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result


# Example 1
intervals = [[1,3], [2,6], [8,10], [15,18]]
print(mergeIntervals(intervals))

# Example 2
intervals = [[1,4], [4,5]]
print(mergeIntervals(intervals))

# Example 3
intervals = [[4,7], [1,4]]
print(mergeIntervals(intervals))
