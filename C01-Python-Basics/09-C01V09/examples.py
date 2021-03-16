def function_name_using_snake_case(argument1, argument2):
    print(argument1, argument2)

    return 42


result = function_name_using_snake_case(1, 2)


def function_without_arguments_or_body():
    pass


result = function_without_arguments_or_body()  # None


a = 1
b = 2


def f(a, b):
    print(a, b)  # 3, 4

    return a + b


result = f(3, 4)  # 7


def g():
    print(a, b)  # 1, 2

    return a + b


result = g()  # 3


def sum1(xs):
    result = 0

    for x in xs:
        result += x

    return result


result = sum1([1, 2, 3])


def sum2(*xs):
    result = 0

    for x in xs:
        result += x

    return result


result = sum2(1, 2, 3)
also_result = sum2(*[1, 2, 3])


def keys1(d):
    result = []

    for key in d:
        result.append(key)

    return result


# ['a', 'b']
result = keys1(
    {
        'a': 1,
        'b': 2
    }
)


def keys2(**d):
    result = []

    for key in d:
        result.append(key)

    return result


# ['a', 'b']
result = keys2(a=1, b=2)

d = {'a': 1, 'b': 2}
# ['a', 'b']
also_result = keys2(**d)
