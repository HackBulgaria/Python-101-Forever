# Video - https://youtu.be/Y8F79VIoomc
def number_to_digits(n):
    n = abs(n)
    digits = []

    char_digits = list(str(n))

    for char_digit in char_digits:
        digits.append(int(char_digit))

    return digits


def is_number_balanced(number):
    #  0  1    2  3
    # [4, 5, | 1, 8] -> even length
    # -----
    #  0  1  2   3   4  5  6
    # [1, 2, 3, |8|, 0, 3, 3] -> odd length
    digits = number_to_digits(number)
    length = len(digits)
    middle = length // 2
    is_odd_length = length % 2 == 1

    left_sum = 0
    right_sum = 0

    for index, digit in enumerate(digits):
        if index < middle:
            left_sum += digit
        else:
            if index == middle and is_odd_length:
                continue

            right_sum += digit

    return left_sum == right_sum


tests = [
    (9, True),
    (4518, True),
    (1111, True),
    (11111, True),
    (28471, False),
    (1238033, True),
    (123, False),
    (121, True),
]


for n, expected in tests:
    result = is_number_balanced(n)

    print(result == expected)
