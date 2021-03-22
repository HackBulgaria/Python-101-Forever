# C01P02 - Sum of digits

Given an integer, implement a function, called `sum_of_digits(n)` that calculates the sum of n's digits.

If a negative number is given, our function should work as if it was positive.

**Here's the signature:**

```python
def sum_of_digits(n):
    pass
```

**Examples:**

```python
sum_of_digits(1325132435356) == 43
sum_of_digits(123) == 6
sum_of_digits(6) == 6
sum_of_digits(-10) == 1
```

**Hints:**

In Python, there is a special operator for integer division:

```python
5 / 2 == 2.5
5 // 2 == 2
```

There's also the standard modulo division:

```python
123 % 10 == 3
```
