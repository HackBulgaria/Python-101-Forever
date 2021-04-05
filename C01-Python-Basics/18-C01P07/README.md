# C01P07 - Increasing and decreasing

Implement a function, called `increasing_or_decreasing(ns)` where `ns` is a list of integers.

The function should return a value from the following [enum](https://docs.python.org/3/library/enum.html):

```python
from enum import Enum


class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3
```

1. It should return `Monotonicity.INCREASING`, if for every two elements, `a` and `b`, that are next to each other, we have `a < b`
1. It should return `Monotonicity.DECREASING`, if for every two elements, `a` and `b`, that are next to each other, we have `a > b`
1. It should return `Monotonicity.NONE` if it's neither increasing nor decrasing.

**Signature**

```python
def increasing_or_decreasing(ns):
    pass
```

**Examples**

```python
increasing_or_decreasing([1, 2, 3, 4, 5]) == Monotonicity.INCREASING
increasing_or_decreasing([5, 6, -10]) == Monotonicity.NONE
increasing_or_decreasing([1, 1, 1, 1]) == Monotonicity.NONE
increasing_or_decreasing([9, 8, 7, 6]) == Monotonicity.DECREASING
increasing_or_decreasing([]) == Monotonicity.NONE
increasing_or_decreasing([1]) == Monotonicity.NONE
increasing_or_decreasing([1, 100]) == Monotonicity.INCREASING
increasing_or_decreasing([1, 100, 100]) == Monotonicity.NONE
increasing_or_decreasing([100, 1]) == Monotonicity.DECREASING
increasing_or_decreasing([100, 1, 1]) == Monotonicity.NONE
increasing_or_decreasing([100, 1, 2]) == Monotonicity.NONE
```
