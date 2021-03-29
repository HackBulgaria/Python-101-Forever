# C01P04 - Char histotgram

Implement a funcion, called `char_histogram(string)`, which takes a string and returns a dictionary, where each key is a character from string and its value is the number of occurrences of that char in the string.

**Here's the signature:**

```python
def char_histogram(string):
    pass
```

**Examples:**

```python
char_histogram("") == {}
char_histogram("    ") = {' ': 4}
char_histogram("Python!") == {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1}
char_histogram("AAAAaaa!!!") == {'A': 4, 'a': 3, '!': 3}
char_histogram("Some very long string here with different casing") ==
{
    'S': 1,
    'o': 2,
    'm': 1,
    'e': 6,
    ' ': 7,
    'v': 1,
    'r': 4,
    'y': 1,
    'l': 1,
    'n': 4,
    'g': 3,
    's': 2,
    't': 3,
    'i': 4,
    'h': 2,
    'w': 1,
    'd': 1,
    'f': 2,
    'c': 1,
    'a': 1
}
```

**Hints:**

1. Membership access check: `key in dict` / `key not in dict`
1. Or you can use the `.get(key, default)` method: `{}.get(key, 0) == 0`
