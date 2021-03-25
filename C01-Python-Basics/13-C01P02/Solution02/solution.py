# Video - https://youtu.be/DB2noiynqfs
def sum_of_digits(n):
    n = abs(n)

    result = 0

    while n != 0:
        digit = n % 10
        result += digit

        n = n // 10

    return result


tests = [
    (1325132435356, 43),
    (123, 6),
    (6, 6),
    (-10, 1),
    (0, 0)
]

for n, expected in tests:
    result = sum_of_digits(n)

    print(result == expected)
