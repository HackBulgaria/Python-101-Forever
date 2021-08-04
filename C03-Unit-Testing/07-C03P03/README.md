# C03P03 - Exception silencing

Implement a context manager called `ExceptionSilencer`, which can be used as follows:

```python
with ExceptionSilencer(ValueError):
    int("aa")

print("We can reach this point, because the exception was not propagated")
```

We want our exception silencer to only silence the specific exception class that we are providing.

For example:

```python
with ExceptionSilencer(Exception):
    int("aa")

print("We cannot reach this point, because the exception was propagated")
```

Alongside the solution, add tests to show that the solution is behaving as expected.

## Hints

1. Have 2 Python files - `exception_silencer.py` and `exception_silencer_tests.py`
2. Consider using the `is` operator.
