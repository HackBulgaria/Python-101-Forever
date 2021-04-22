# C01P14 - Goldbach conjecture
# Video - https://youtu.be/PeUJzKFh2sQ

from itertools import combinations_with_replacement


def is_prime(n):
    if n < 2:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False

    return True


def goldbach(n):
    if n <= 2 or n % 2 == 1:
        return

    result = []

    # List comprehension
    primes = [x for x in range(2, n) if is_prime(x)]

    for p1, p2 in combinations_with_replacement(primes, 2):
        if p1 + p2 == n:
            result.append((p1, p2))

    return result


tests = [
    (4, [(2, 2)]),
    (6, [(3, 3)]),
    (8, [(3, 5)]),
    (10, [(3, 7), (5, 5)]),
    (100, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]),
    (5, None)
]

for n, expected in tests:
    result = goldbach(n)

    print(result == expected)
