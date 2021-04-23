# C01P15 - Gas stations
# Video - https://youtu.be/mlPfHta9Lus

# 90,      [50, 80, 140, 180, 220, 290], 320
# diffs    [50, 30, 60,  40,  40,  70,   30]
# gas_tank [40, 90, 30,  50,  90,  90,   60]
def gas_stations(distance, tank_size, stations):
    result = []

    stations_with_target = [
        station for station in stations
        if station < distance
    ] + [distance]
    diffs = [stations_with_target[0]]

    for index in range(0, len(stations_with_target) - 1):
        diffs.append(
            stations_with_target[index + 1] - stations_with_target[index]
        )

    current_tank_size = tank_size

    for index, diff in enumerate(diffs):
        current_tank_size -= diff

        # Cannot reach 50km with 50l
        if current_tank_size <= 0:
            current_tank_size = tank_size - diff

            if current_tank_size <= 0:
                return []

            result.append(stations[index - 1])

    return result


tests = [
    ((320, 90, [50, 80, 140, 180, 220, 290]), [80, 140, 220, 290]),
    ((390, 80, [70, 90, 140, 210, 240, 280, 350]), [70, 140, 210, 280, 350]),
    ((100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]), [40, 80]),
    ((100, 101, [200]), []),
    ((100, 50, [200]), []),
    ((100, 50, [10, 90]), []),
]

for args, expected in tests:
    result = gas_stations(*args)

    passing = result == expected

    if passing:
        print(passing)
    else:
        print(passing, result)
