# C01P11 - Anagrams

According to [Wikipedia](https://en.wikipedia.org/wiki/Anagram), we have the following definition of an anagram:

> An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

For example, `listen` and `silent` are anagrams.

Implement a function called `anagrams`, that takes `word1, word2` and returns `True`, if those words are anagrams and `False` otherwise.

We should take the following into consideration:

1. Casing does not matter, meaning `LISTEN` and `silent` are anagrams.
1. Whitespace does not matter, meaning `New York Times` and `monkeys writting` are anagrams.

**Signature**

```python
def anagrams(word1, word2):
    pass
```

**Examples**

```python
anagrams("listen", "silent") is True
anagrams("LISTEN", "silent") is True
anagrams("python", "ruby") is False
anagrams("New York Times", "monkeys write") is True
anagrams("snake", "sssnakee") is False
```
