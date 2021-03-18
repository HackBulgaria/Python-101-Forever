a = 1
b = a

print(
    id(a) == id(b)  # True
)

a = 2
print(
    id(a) == id(b)  # False
)

print(a, b)  # 2, 1


a = [1, 2, 3]
b = a

print(
    id(a) == id(b)  # True
)

a = [3, 4, 5]
print(
    id(a) == id(b)  # False
)

print(a, b)  # [3, 4, 5], [1, 2, 3]

a = [1, 2, 3]
b = a

print(
    id(a) == id(b)  # True
)

b.append(4)

print(
    id(a) == id(b)  # True
)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]


a = [1, 2, 3]
b = [1, 2, 3]

print(
    a == b  # True
)

print(
    a is b  # False
)

print(
    id(a) == id(b)  # False
)

a = True
b = True

print(
    a == b  # True
)

print(
    a is b  # True
)

print(
    id(a) == id(b)  # True
)
