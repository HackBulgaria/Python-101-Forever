# https://youtu.be/BpoFDMIp3Fg

def string_reverse(s):
    return ''.join(reversed(s))


def is_integer_palindrome(x):
    # TODO: integer reverse
    x = str(x)

    return x == string_reverse(x)


def build_cache():
    result = {}

    n = 99999

    for x in range(10, n + 1):
        result[x] = is_integer_palindrome(x)

    return result


CACHE = build_cache()


def palindromes_count(n):
    # 11 (11), 10 (01), 101 (101)
    count = 0

    for x in range(10, n + 1):
        if CACHE[x]:
            count += 1

    return count


tests = [
    (10, 0),
    (20, 1),
    (30, 2),
    (101, 10),
    (200, 19),
    (43539, 525),
    (4247, 132),
    (48877, 577),
    (94012, 1029),
    (62560, 715),
    (92009, 1009),
    (63176, 721),
    (67409, 763),
    (62834, 718),
    (77420, 863),
    (99999, 1089),
]


for n, expected in tests:
    result = palindromes_count(n)

    print(result == expected)
