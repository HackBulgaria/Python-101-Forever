# Video - https://youtu.be/p9A5ySU8nWU

def to_digits(number):
    digits = []

    for x in str(number):
        digits.append(int(x))

    return digits


# 79927398713
# 7 + 9 + 9 + 4 + 7 + 6 + 9 + 7 + 7 + 2 + 3
def is_credit_card_valid(number):
    result = []

    digits = to_digits(number)
    digits_count = len(digits)

    double = False

    for index in range(digits_count - 1, -1, -1):
        multiplier = 1

        if double:
            multiplier = 2

        transformed = sum(to_digits(digits[index] * multiplier))

        result.append(transformed)

        double = not double

    return sum(result) % 10 == 0


tests = [
    (79927398713, True),
    (4417123456789113, True),
    (4242424242424242, True),
    (79927398715, False),
    (79927398710, False),
    (79927398711, False),
    (79927398712, False),
    (79927398714, False),
    (79927398715, False),
    (79927398716, False),
    (79927398717, False),
    (79927398718, False),
    (79927398719, False)
]


for number, expected in tests:
    result = is_credit_card_valid(number)

    print(result == expected)
