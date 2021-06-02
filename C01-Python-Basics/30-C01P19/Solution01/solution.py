from copy import deepcopy

# SCREAMING_SNAKE_CASE
MOVEMENTS = {
    "A": (-1, 0),
    "B": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}


def outside_of_bounds(point, matrix):
    x, y = point

    MIN_X = 0
    MAX_X = len(matrix) - 1

    MIN_Y = 0
    MAX_Y = len(matrix[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y


def add_points(p, q):
    px, py = p
    qx, qy = q

    return (px + qx, py + qy)


def print_layout(configuration, layout):
    layout = deepcopy([list(row) for row in layout])

    for name, point in configuration.items():
        x, y = point
        layout[x][y] = name

    for row in layout:
        print("".join(row))


def build_layout(configuration, layout):
    layout = deepcopy([list(row) for row in layout])

    for name, point in configuration.items():
        x, y = point
        layout[x][y] = name

    new_layout = []

    for row in layout:
        new_layout.append("".join(row))

    return new_layout


def in_cinema(point, cinema_layout):
    x, y = point

    return (
        # short circuit
        not outside_of_bounds(point, cinema_layout)
        and cinema_layout[x][y] == "."
    )


def build_friends_relative_position(friends_configuration):
    relative_position = {}

    for configuration in friends_configuration:
        relative_position[configuration[0]] = (0, 0)

    for configuration in friends_configuration:
        if len(configuration) == 1:
            continue

        name, position, relative_to = configuration

        relative_x, relative_y = relative_position[relative_to]
        dx, dy = MOVEMENTS[position]

        relative_position[name] = (relative_x + dx, relative_y + dy)

    return relative_position


def stranger_forms(cinema_layout, friends_configuration):
    result = []
    friends_relative_position = build_friends_relative_position(
        friends_configuration
    )

    for x in range(len(cinema_layout)):
        for y in range(len(cinema_layout[0])):
            if cinema_layout[x][y] == "*":
                continue

            # Do we satisfy friends_configuration for (x, y)
            # If yes, build new layout with configuration
            # Push to result
            friends_current_position = {
                name: add_points((x, y), relative_point)
                for name, relative_point in friends_relative_position.items()
            }

            # Dict comprehension above is the same as:
            # friends_current_position = {}
            # for name, point in friends_relative_position.items():
            #     friends_current_position[name] = add_points((x, y), point)

            all_points_in = True

            for point in friends_current_position.values():
                if not in_cinema(point, cinema_layout):
                    all_points_in = False
                    break

            if all_points_in:
                print_layout(friends_current_position, cinema_layout)
                print('---------------------------------')

                result.append(
                    build_layout(
                        friends_current_position,
                        cinema_layout
                    )
                )

    return result


cinema_layout = [
    '..*...*.**',
    '.....**...',
    '*.*...*..*',
    '.**....*.*',
    '...*..*.*.',
    '.***...*..',
    '*......*.*',
    '.....**..*',
    '..*.*.*..*',
    '***.*.**..'
]

friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]

stranger_forms(cinema_layout, friends_configuration)
