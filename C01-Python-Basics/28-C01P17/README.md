# C01P17 - Word counter

You are given a matrix (list of lists) with chars & an additional `word`.

Your task is to count the occurences of that `word` in the table.

The word can be found: 

- horizontaly
- vertically
- across both left to right and right to left.



For example, lets count the word `ivan` in the table:

| i   | v   | a   | n   |
| --- | --- | --- | --- |
| e   | _v_ | _n_ | h   |
| i   | n   | _a_ | v   |
| m   | v   | _v_ | _n_ |
| q   | r   | _i_ | t   |


We count exactly `3` occurences of the word.

Implement a function `word_counter` that does exactly that.

**Signature**

```python
def word_counter(matrix, word):
    pass
```

**Examples**

```python
word = "ivan"
matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]
word_counter(matrix, word) == 3
```

```python
word = "actually"
matrix = [
    ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],
    ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],
    ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],
    ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],
    ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],
    ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],
    ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]
]
word_counter(matrix, word) == 4
```

```python
word = "madam"
matrix = [
    ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
    ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
    ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
    ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
    ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
    ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
    ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
]
word_counter(matrix, word) == 3
```

```python
word = "python"
matrix = [
  ["r", "u", "b", "y"],
  ["r", "u", "b", "y"],
  ["r", "u", "b", "y"],
  ["r", "u", "b", "y"],
]

word_counter(matrix, word) == 0
```
