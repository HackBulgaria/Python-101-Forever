from pprint import pprint

from copy import deepcopy


def sum_matrix(matrix):
    return sum(sum(row) for row in matrix)


def outside_of_bounds(point, matrix):
    x, y = point

    MIN_X = 0
    MAX_X = len(matrix) - 1

    MIN_Y = 0
    MAX_Y = len(matrix[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y


def bomb_matrix(point, matrix):
    # -1, 0, 1 без (0, 0)
    moves = [
        (0, 1),
        (1, 0),

        (1, 1),
        (-1, -1),

        (-1, 1),
        (1, -1),

        (-1, 0),
        (0, -1)
    ]

    point_x, point_y = point
    bomb_value = matrix[point_x][point_y]

    points = [
        (point_x + move[0], point_y + move[1])
        for move in moves
    ]

    for x, y in points:
        if outside_of_bounds((x, y), matrix):
            continue

        current_value = matrix[x][y]
        new_value = current_value - bomb_value

        matrix[x][y] = max(0, new_value)

    return sum_matrix(matrix)


def home_grown_matrix_deepcopy(matrix):
    result = []

    for row in matrix:
        new_row = []

        for item in row:
            new_row.append(item)

        result.append(new_row)

    return result


def matrix_bombing_plan(matrix):
    result = {}

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            point = (x, y)
            pprint(matrix)
            result[point] = bomb_matrix(point, deepcopy(matrix))

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

expected = {
    (0, 0): 42,
    (0, 1): 36,
    (0, 2): 37,
    (1, 0): 30,
    (1, 1): 15,
    (1, 2): 23,
    (2, 0): 29,
    (2, 1): 15,
    (2, 2): 26
}

result = matrix_bombing_plan(matrix)

print(result == expected)
# pretty print
pprint(result)
