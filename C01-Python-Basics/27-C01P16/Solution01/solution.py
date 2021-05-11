# C01P16 - Nokia keypad


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


KEYPAD = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}


def numbers_to_message(pressed_sequence):
    letters = []
    grouped_pressed_sequence = group(pressed_sequence)

    upper = False

    for grouped in grouped_pressed_sequence:
        key = grouped[0]
        times_pressed = len(grouped)

        if key == -1:
            continue

        if key == 1:
            upper = True
            continue

        if key == 0:
            letters.append(" " * times_pressed)
            continue

        sequence = KEYPAD[key]
        letter = sequence[(times_pressed - 1) % len(sequence)]

        if upper:
            letter = letter.upper()
            upper = False

        letters.append(letter)

    return "".join(letters)


tests = [
    (
        [0, 0, 0, 0],
        "    "
    ),
    (
        [2, -1, 2, 2, -1, 2, 2, 2],
        "abc"
    ),
    (
        [2, 2, 2, 2],
        "a"
    ),
    (
        [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2],  # noqa
        "Ivo e Panda"
    ),
    (
        [2, 3, 4, 5, 6, 7, 8, 9],
        "adgjmptw"
    ),
    (
        [2, -1, 3,-1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1, 9],  # noqa
        "adgjmptw"
    ),
    (
        [0, -1, 0, -1, 0, -1, 0],
        "    "
    ),
    (
        [2, 2, 2, -1, 2],
        "ca"
    ),
]

for sequence, expected in tests:
    result = numbers_to_message(sequence)

    print(result == expected, result)
