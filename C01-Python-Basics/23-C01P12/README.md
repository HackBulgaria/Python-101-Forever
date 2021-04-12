# C01P12 - Credit card validation

Implement a function, called `is_credit_card_valid(number)`, which returns `True` or `False` based on the following algorithm:

1. Starting from the right, double every second digit.
  1. If after doubling the digit becomes `>= 10`, calculate the sum of the digits of the new number & use that. For example, if we have `9` and doubling it gets us `18`, the final result is going to be `1 + 8 = 9`
1. After the transformation, we find the sum of all digits in the transformed number.
1. The number is valid, if the sum is divisible by 10.

This is also known as the [Luhn algorithm.](https://en.wikipedia.org/wiki/Luhn_algorithm)

For example: `79927398713` is valid, bacause:

1. After doubling, we get the following number:

```
                7 +
sum_digits(9 * 2) +
                9 +
sum_digits(2 * 2) +
                7 +
sum_digits(3 * 2) +
                9 +
sum_digits(8 * 2) +
                7 +
sum_digits(1 * 2) +
                3
```

2. And calculating the sum of the digits of the transformed number, we get `70` => the card number is valid.


**Signature**

```python
def is_credit_card_valid(number):
    pass
```

**Examples**

```python
is_credit_card_valid(79927398713) is True
is_credit_card_valid(79927398715) is False
is_credit_card_valid(4417123456789113) is True
```

In case you need more cards, you can check out [Stripe testing cards](https://stripe.com/docs/testing)
