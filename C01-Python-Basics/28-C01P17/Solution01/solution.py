import enum


class Direction(enum.Enum):
    HORIZONTAL_LEFT = "HORIZONTAL_LEFT"
    HORIZONTAL_RIGHT = "HORIZONTAL_RIGHT"

    VERTICAL_LEFT = "VERTICAL_LEFT"
    VERTICAL_RIGHT = "VERTICAL_RIGHT"

    DIAGONAL_UP_RIGHT = "DIAGONAL_UP_RIGHT"
    DIAGONAL_UP_LEFT = "DIAGONAL_UP_LEFT"

    DIAGONAL_DOWN_RIGHT = "DIAGONAL_DOWN_RIGHT"
    DIAGONAL_DOWN_LEFT = "DIAGONAL_DOWN_LEFT"


def take_word(n, point, direction, matrix):
    # dx, dy
    if direction == Direction.DIAGONAL_UP_LEFT:
        pass


def word_counter(matrix, word):
    result = 0

    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[0])):
            for direction in Direction:
                found_word = take_word(
                    len(word),
                    (row_index, column_index),
                    direction,
                    matrix,
                )

                if found_word == word:
                    result += 1

    # TODO: Test this
    if word == word[::-1]:
        result = result // 2

    return result


word = "ivan"
matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]

matrix[2][3]
word_counter(matrix, word) == 3

word = "actually"
matrix = [
    ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],  # noqa
    ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],  # noqa
    ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],  # noqa
    ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],  # noqa
    ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],  # noqa
    ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],  # noqa
    ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],  # noqa
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]   # noqa
]
word_counter(matrix, word) == 4

word = "madam"
matrix = [
    ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
    ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
    ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
    ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
    ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
    ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
    ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
]
word_counter(matrix, word) == 3
