# C01P01 - IBAN formatter

Someone is emailing you an invoice. You grab the "windows machine" and open up the online banking.

It's time to type the provided IBAN. And to be frank - IBANs are really hard to read.

You get something like that:

```
BG80BNBG96611020345678
```

A bunch of numbers and letters that are hard to look at & type elsewhere.

But if you somehow manage to get the IBAN to look like that:

```
BG80 BNBG 9661 1020 3456 78
```

It's quite easy to type that elsewhere, because everyting is split in groups of 4 numbers & there's nice whitespace.

**Your task is to implement the following Python function:**

```python
def iban_formatter(iban):
    pass
```

1. The function takes a string (an IBAN) and returns the IBAN in the formatted way showed above.
1. Keep in mind that the IBAN can be already formatted & the function should take care of that too.

**Examples:**

```python
iban_formatter("BG80BNBG96611020345678") == "BG80 BNBG 9661 1020 3456 78"
iban_formatter("BG80 BNBG 9661 1020 3456 78") == "BG80 BNBG 9661 1020 3456 78"
iban_formatter("BG14TTBB94005362446381") == "BG14 TTBB 9400 5362 4463 81"
iban_formatter("BG91UNCR70001864961754") == "BG91 UNCR 7000 1864 9617 54"
```

**Hints:**

1. Think of `''.join(xs)` - <https://docs.python.org/3/library/stdtypes.html#str.join>
1. Think of `string.replace(x, y)` - <https://docs.python.org/3/library/stdtypes.html#str.replace>
