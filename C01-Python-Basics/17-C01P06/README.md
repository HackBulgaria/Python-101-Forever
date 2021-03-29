# C01P06 - NaN expand

In most programming languages, NaN stands for Not a Number.

If we take a look at the following JavaScript code:

```javascript
typeof NaN === 'number'; // true
```

We will see that in JavaScript, `NaN` stands for `Not a NaN`, which is recursive by nature.

Implement a Python function, called `nan_expand(times)`, which returns the expansion of `NaN` (In JavaScript terms) that many `times`.

**Here's the signature:**

```python
def nan_expand(times):
    pass
```

**Examples:**

1. If we expand NaN once (`times=1`), we will have `"Not a NaN"`
1. If we expand NaN twice (`times=2`), we will have `"Not a Not a NaN"`
1. If `times=3`, we have `"Not a Not a Not a NaN"`
1. And so on ...

```python
nan_expand(0) == ""
nan_expand(1) == "Not a NaN"
nan_expand(2) == "Not a Not a NaN"
nan_expand(3) == "Not a Not a Not a NaN"
```
