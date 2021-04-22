# C01P14 - Goldbach conjecture
# Video - https://youtu.be/f2PsNBHR73o

def is_prime(n):
    if n < 2:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False

    return True


# Every even integer greater than 2
# can be expressed as the sum of two primes.
def goldbach(n):
    if n <= 2 or n % 2 == 1:
        return

    result = []

    # List comprehension
    primes = []

    for x in range(2, n):
        if is_prime(x):
            primes.append(x)

    # a + b == b + a
    used = set()

    for p1 in primes:
        for p2 in primes:
            if p1 + p2 == n:
                pair = (p1, p2)
                reverse_pair = (p2, p1)

                if pair not in used and reverse_pair not in used:
                    used.add(pair)
                    result.append(pair)

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
