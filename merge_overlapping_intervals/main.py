# You are given an array of intervals - that is, an array of tuples (start, end).
# The array may not be sorted, and could contain overlapping intervals.
# Return another array where the overlapping intervals are merged.

# For example:
# [(1, 3), (5, 8), (4, 10), (20, 25)]

# This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

def merge_intervals(a, b):
    return [a[0], b[1]] if a[0] < b[0] < a[1] < b[1] \
        else [b[0], a[1]] if b[0] < a[0] < b[1] < a[1] \
        else [a[0], a[1]] if a[0] < b[0] < b[1] < a[1] \
        else [b[0], b[1]] if b[0] < a[0] < a[1] < b[1] \
        else None


def merge(intervals):
    output = []
    for interval in intervals:
        i = 0
        merged = None
        while merged is None and i < len(output):
            merged = merge_intervals(interval, output[i])
            if merged is not None:
                output[i] = merged
            i += 1
        if merged is None:
            output.append(interval)

    return output


print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
print(merge([(1, 7), (5, 8), (6, 10), (9, 25)]))
[[1, 25]]
