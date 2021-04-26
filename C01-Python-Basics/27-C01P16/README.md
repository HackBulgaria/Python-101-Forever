# C01P16 - Nokia keypad

A long time ago, before the smartphones, when you had to write some messages, the keypads looked like that:

![Nokia Keypad](https://user-images.githubusercontent.com/387867/116038228-d92c3380-a671-11eb-8e31-ff902ada6771.jpg)

For example, on such keypad, if you want to write **Ruby**, you had to press the following sequence of numbers:

```
7778822999
```

Each key contains some letters from the alphabet. And by pressing that key, you rotate the letters until you get to your desired one.

It's time to implement some encode / decode functions for the old keypads!

First, implement a function that takes a list of integers - the sequence of numbers that have been pressed. The returned value should be the corresponding string of the message.

**Signature**

```python
def numbers_to_message(pressed_sequence):
    pass
```

There are some special rules:

-   If you press `1`, the next letter is going to be capitalized
-   If you press `0`, this will insert a single white-space
-   If you press a number and wait for a few seconds, the special breaking number `-1` enters the sequence. This is the way to write different letters from only one keypad!

**Examples:**

```python
>>> numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])
"abc"
>>> numbers_to_message([2, 2, 2, 2])
"a"
>>> numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])
"Ivo e Panda"
```

Now it is time to convert the message to a sequence of numbers. This function takes a string - the `message` and returns the **minimal** keystrokes that you need to write that `message`

**Signature**

```python
def message_to_numbers(message):
    pass
```

**Examples**

```python
>>> message_to_numbers("abc")
[2, -1, 2, 2, -1, 2, 2, 2]
>>> message_to_numbers("a")
[2]
>>> message_to_numbers("Ivo e Panda")
[1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
>>> message_to_numbers("aabbcc")
[2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]
```
