import enum


class Direction(enum.Enum):
    HORIZONTAL_RIGHT = "HORIZONTAL_RIGHT"
    HORIZONTAL_LEFT = "HORIZONTAL_LEFT"

    VERTICAL_DOWN = "VERTICAL_DOWN"
    VERTICAL_UP = "VERTICAL_UP"

    DIAGONAL_UP_RIGHT = "DIAGONAL_UP_RIGHT"
    DIAGONAL_UP_LEFT = "DIAGONAL_UP_LEFT"

    DIAGONAL_DOWN_RIGHT = "DIAGONAL_DOWN_RIGHT"
    DIAGONAL_DOWN_LEFT = "DIAGONAL_DOWN_LEFT"


def outside_of_bounds(point, matrix):
    x, y = point

    MIN_X = 0
    MAX_X = len(matrix) - 1

    MIN_Y = 0
    MAX_Y = len(matrix[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y


def take_word(n, point, direction, matrix):
    dx = 0
    dy = 0

    direction_mapper = {
        Direction.HORIZONTAL_RIGHT: (0, 1),
        Direction.HORIZONTAL_LEFT: (0, -1),

        Direction.VERTICAL_DOWN: (1, 0),
        Direction.VERTICAL_UP: (-1, 0),

        Direction.DIAGONAL_UP_RIGHT: (-1, 1),
        Direction.DIAGONAL_UP_LEFT: (-1, -1),

        Direction.DIAGONAL_DOWN_RIGHT: (1, 1),
        Direction.DIAGONAL_DOWN_LEFT: (1, -1),
    }

    dx, dy = direction_mapper.get(direction, (0, 0))

    # grunt work
    # if direction == Direction.HORIZONTAL_RIGHT:
    #     dx = 0
    #     dy = 1

    # if direction == Direction.HORIZONTAL_LEFT:
    #     dx = 0
    #     dy = -1

    # if direction == Direction.VERTICAL_DOWN:
    #     dx = 1
    #     dy = 0

    # if direction == Direction.VERTICAL_UP:
    #     dx = -1
    #     dy = 0

    # if direction == Direction.DIAGONAL_UP_RIGHT:
    #     dx = -1
    #     dy = 1

    # if direction == Direction.DIAGONAL_UP_LEFT:
    #     dx = -1
    #     dy = -1

    # if direction == Direction.DIAGONAL_DOWN_RIGHT:
    #     dx = 1
    #     dy = 1

    # if direction == Direction.DIAGONAL_DOWN_LEFT:
    #     dx = 1
    #     dy = -1

    start_x, start_y = point
    n_counter = 0
    chars = []

    while n_counter != n:
        if outside_of_bounds((start_x, start_y), matrix):
            # However we decide to define it
            # can be break
            return None

        chars.append(matrix[start_x][start_y])

        start_x += dx
        start_y += dy

        n_counter += 1

    return "".join(chars)


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

result = word_counter(matrix, word)
print(result == 3, result)

word = "actually"
matrix = [
    ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],  # noqa
    ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],  # noqa
    ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],  # noqa
    ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],  # noqa
    ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],  # noqa
    ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],  # noqa
    ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],  # noqa
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]  # noqa
]
result = word_counter(matrix, word)
print(result == 4, result)

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
result = word_counter(matrix, word)
print(result == 3, result)
