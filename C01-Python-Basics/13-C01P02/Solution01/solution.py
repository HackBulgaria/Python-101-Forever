# Video - https://youtu.be/PmW8NfctNpk
def sum_of_digits(n):
    n = abs(n)
    digits = []

    char_digits = list(str(n))

    for char_digit in char_digits:
        digits.append(int(char_digit))

    return sum(digits)


tests = [
    (1325132435356, 43),
    (123, 6),
    (6, 6),
    (-10, 1)
]

for n, expected in tests:
    result = sum_of_digits(n)

    print(result == expected)
