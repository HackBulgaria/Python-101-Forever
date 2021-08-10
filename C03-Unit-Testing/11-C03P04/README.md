# C03P04 - Fractions

You are given the following empty class:

```python
class Fraction:
    def __init__(self, numerator, denominator):
        """
        Construct a new Fraction.

        If denominator = 0, raise ValueError.
        """
        pass

    def __str__(self):
        """
        Returns the string representation of self.
        """

    def __repr__(self):
        """
        Returns the REPL representation of self.
        """

    def __eq__(self, other):
        """
        Returns True/False, if self is equal to other.
        """

    def __add__(self, other):
        """
        Returns new Fraction, that's the sum of self and other.
        """

    def __sub__(self, other):
        """
        Returns new Fraction, that's the substraction of self and other.
        """

    def __mul__(self, other):
        """
        Returns new Fraction, that's the product of self and other.
        """

    def simplify(self):
        """
        Returns new Fraction, that's the simplification of self
        """

    def is_simplified(self):
        """
        Returns True/False, if self cannot be simplified further
        """
```

This class defines a basic interfaces for a fraction.

**Your task is to implement all methods & add unit tests accordingly.**

1. The implementation of `Fraction` should live in `fraction.py`.
1. The tests should live in `fraction_tests.py`.

## Examples of behavior

```python
a = Fraction(1, 2)
b = Fraction(1, 2)

print(a == b)  # True

print(a)  # 1/2
print(b)  # 1/2

c = a + b

print(a)  # 1/2
print(b)  # 1/2
print(c)  # 2/2

print(c.simplify())  # 1/1
print(c)  # 2/2

print(c.is_simplified())  # False
print(c.simplify().is_simplified())  # True

d = a - b
print(d)  # 0
print(d.simplify())  # 0
print(d.is_simplified())  # True

e = a * b
print(e)  # 1/4
print(e.simplify())  # 1/4
print(e.is_simplified())  # True
```

## Extra credit

Add additional methods to `Fraction`, so a list of fractions can be sorted:

```python
sorted([Fraction(3, 4), Fraction(1, 2)]) == [Fraction(1, 2), Fraction(3, 4)]
```
