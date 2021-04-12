# C01P10 - Palindromes count

Implement a function called `palindromes_count`, which:

1. Takes a number `n`.
1. Returns the number of integer palindromes between `[10, n]`.
1. It's important to note that: `10 <= n <= 99999`.

An integer palindrome is a number `x`, that written in reverse, remains the same.

For example, `11` is a palindrome, but `10` is not.

**Signature**

```python
def palindromes_count(n):
    pass
```

**Examples**

```python
palindromes_count(10) == 0
palindromes_count(20) == 1  # only 11
palindromes_count(101) == 10  # 11, 22, 33, 44, 55, 66, 77, 88, 99, 101
palindromes_count(92009) == 1009
palindromes_count(99999) == 1089
```
