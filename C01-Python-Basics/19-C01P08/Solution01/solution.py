# Video - https://youtu.be/EzP6vfASVo0

def group(items):
    result = []
    length = len(items)
    index = 0

    while index < length:
        item = items[index]
        current_group = [item]

        lookup_index = index + 1

        while lookup_index < length and items[lookup_index] == item:
            current_group.append(items[lookup_index])
            lookup_index += 1

        result.append(current_group)
        index = lookup_index

    return result


tests = [
    ([1, 1, 1, 2, 3, 1, 1], [[1, 1, 1], [2], [3], [1, 1]]),
    ([1, 2, 1, 2, 3, 3], [[1], [2], [1], [2], [3, 3]]),
    ([], []),
    ([1], [[1]]),
    ([1, 1, 1, 1], [[1, 1, 1, 1]]),
    ([1, 2, 3, 4], [[1], [2], [3], [4]])
]

for items, expected in tests:
    result = group(items)

    print(result == expected)
