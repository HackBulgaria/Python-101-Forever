# Tuples - immutable lists with fixed size

a_list = [1, 2, 3]
a_tuple = (1, 2, 3)
a_tuple_with_one_element = (1,)

# We cannot mutate a tuple:
# a_tuple[0] = 111

# We cannot add elements to a tuple
# a_tuple.append(111)

# We can omit the ()
another_tuple = 1, 2, 3

print(a_tuple)
print(another_tuple)

print(a_tuple == another_tuple)


# We can loop in a standard manner over a tuple
for x in a_tuple:
    print(x)


print(1 in (1, 2, 3))  # True
print(1 in (2, 3))  # False
print(1 in ())  # False
print(1 not in ())  # True


print((1) == (1,))  # False
