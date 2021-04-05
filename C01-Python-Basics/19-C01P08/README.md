# C01P08 - Group

We are going to implement a very helpful function, called `group`.

`group` takes a list of items and returns a list of groups, where each group is formed by **all equal consecutive elements in the list.**

**Signature**

```python
def group(items):
    pass
```

**Examples**

```python
group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]]
group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]]
group([]) == []
group([1]) == [[1]]
group([1, 1, 1, 1]) == [[1, 1, 1, 1]]
```
