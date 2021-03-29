# C01P05 - Sum matrix

You are given a NxM matrix of integer numbers.

Implement a function, called `sum_matrix(m)` that returns the sum of all numbers in the matrix.

The matrix will be represented as nested lists in Python.

**Here's the signature:**

```python
def sum_matrix(m):
    pass
```

**Examples:**

```python
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_matrix(m) == 45

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_matrix(m) == 0

m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
sum_matrix(m) == 55
```

**Hints:**

1. You can easily nest for-loops.
