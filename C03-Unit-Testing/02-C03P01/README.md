# C03P01 - Interval extended

In `C03V01`, we showed the `Interval` class.

We want to extend the interval class, so it is aware of open & closed intervals.

Finish up the implementation of this:

```python
class Interval:
    def __init__(self, start, end, start_opened=False, end_opened=False):
        # This is the constructor
        pass

    def is_inside(self, value):
        pass

    def stringify(self):
        pass
```

So it satisfies the following examples:

```python
closed_interval = Interval(1, 10)

closed_interval.is_inside(1) is True
closed_interval.is_inside(5) is True
closed_interval.is_inside(10) is True

closed_interval.stringify() == "[1, 10]
```

and

```python
opened_interval = Interval(1, 10, start_opened=True, end_opened=True)

opened_interval.is_inside(1) is False
opened_interval.is_inside(5) is True
opened_interval.is_inside(10) is False

opened_interval.stringify() == "(1, 10)"
```

and

```python
half_opened_interval = Interval(1, 10, start_opened=False, end_opened=True)

half_opened_interval.is_inside(1) is True
half_opened_interval.is_inside(5) is True
half_opened_interval.is_inside(10) is False

half_opened_interval.stringify() == "[1, 10)"
```

and

```python
half_opened_interval = Interval(1, 10, start_opened=True, end_opened=False)

half_opened_interval.is_inside(1) is False
half_opened_interval.is_inside(5) is True
half_opened_interval.is_inside(10) is True

half_opened_interval.stringify() == "(1, 10]"
```
