# C01P18 - Matrix bombing

You are given a `NxM` matrix of integer numbers.

We can drop a bomb at any place in the matrix, which has the following effect:

- All of the **3 to 8 neighbours** (depending on where you hit!) of the target are reduced by the value of the target.
- Numbers can be reduced only to 0 - they cannot go to negative.

For example, if we have the following matrix:

```
10  10  10
10   9  10
10  10  10
```

and we drop bomb at `9`, this will result in the following matrix:

```
1 1 1
1 9 1
1 1 1
```

Implement a function called `matrix_bombing_plan(m)`.

The function should return a dictionary where keys are positions in the matrix, represented as tuples, and values are the total sum of the elements of the matrix, after the bombing at that position.

The positions are the standard indexes, starting from `(0, 0)`

For example if we have the following matrix:

```
1 2 3
4 5 6
7 8 9
```

and run the function, we will have:

```python
{(0, 0): 42,
 (0, 1): 36,
 (0, 2): 37,
 (1, 0): 30,
 (1, 1): 15,
 (1, 2): 23,
 (2, 0): 29,
 (2, 1): 15,
 (2, 2): 26}
```
