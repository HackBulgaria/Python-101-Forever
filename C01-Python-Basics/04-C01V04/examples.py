languages = []

languages.append("Java")
languages.append("Python")
languages.append("C#")
languages.append("Ruby")

print(languages)

numbers = [1, 2, 3]

imdb_top_3 = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Godfather: Part II"
]

print(imdb_top_3)

empty = []
mixed = [1, True, "Three", [], None]

print(mixed)

# len is a "built-in" function
# more on them, here - https://docs.python.org/3/library/functions.html
if len(empty) == 0:
    print("Empty list check with len")

# bool([]) == False
# bool([1]) == True
if numbers:
    print("Numbers is non-empty")


if not empty:
    print("empty is empty")


# How to check if a given value exists in a list
if 1 in numbers:
    print("1 is in numbers")


if 10 not in numbers:
    print("10 is not in numbers")


for n in numbers:
    print(n)


for movie in imdb_top_3:
    print(movie)


for nothing in empty:
    print(nothing)


for item in mixed:
    print(item)


# Lists have standard index access
print(numbers[0])

# Lists can be mutated
print(numbers)
numbers[0] = 111
print(numbers)

print(empty)
empty.append("Something")
print(empty)


# We can easily compare lists
# Two lists xs & ns are equal, if
# xs[i] == ns[i] for every index i of that lists
# or if both xs & ns are empty
print([] == [])
print([1] == [])
print([1, 2] == [2, 1])
