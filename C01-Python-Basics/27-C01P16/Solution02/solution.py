SEQUENCES = {
    "a": [2],
    "b": [2, 2],
    "c": [2, 2, 2],
    "d": [3],
    "e": [3, 3],
    "f": [3, 3, 3],
    "g": [4],
    "h": [4, 4],
    "i": [4, 4, 4],
    "j": [5],
    "k": [5, 5],
    "l": [5, 5, 5],
    "m": [6],
    "n": [6, 6],
    "o": [6, 6, 6],
    "p": [7],
    "q": [7, 7],
    "r": [7, 7, 7],
    "s": [7, 7, 7, 7],
    "t": [8],
    "u": [8, 8],
    "v": [8, 8, 8],
    "w": [9],
    "x": [9, 9],
    "y": [9, 9, 9],
    "z": [9, 9, 9, 9],
    " ": [0]
}


def message_to_numbers(message):
    sequence = []

    for char in message:
        if char.isupper():
            sequence.append(1)

        shortest_sequence = SEQUENCES[char.lower()]

        if len(sequence) > 0:
            previous_key = sequence[len(sequence) - 1]

            # In case we have "abc", we want to add -1 as a separator
            # That's why we are looking behind to check the previous key
            if previous_key == shortest_sequence[0]:
                sequence.append(-1)

        sequence.extend(shortest_sequence)

    return sequence


tests = [
    ("abc", [2, -1, 2, 2, -1, 2, 2, 2]),
    ("a", [2]),
    ("Ivo e Panda", [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]),  # noqa
    ("aabbcc", [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2])
]


for message, expected in tests:
    result = message_to_numbers(message)

    print(result == expected, result)
