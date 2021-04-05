# C01P09 - Balanced numbers

A number is called balanced, if we take the middle of it and the sums of the left and right parts are equal.

For example, the number `1238033` is balanced, because it's left part is `123` and right part is `033`.

We have: `1 + 2 + 3 = 0 + 3 + 3 = 6`

**Note: A number with only one digit is always balanced!**

**Signature**

```python
def is_number_balanced(number):
    pass
```

**Examples**

```python
is_number_balanced(9) is True
is_number_balanced(4518) is True
is_number_balanced(28471) is False
is_number_balanced(1238033) is True
```
