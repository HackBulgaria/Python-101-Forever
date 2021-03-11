# 1. Multiple assignments

x, y = (1, 2)
print(x, y)

x, y = [1, 2]
print(x, y)

x, y = {'key1': 'value1', 'key2': 'value2'}
print(x, y)

x, y = {1, 2}
print(x, y)


d = {
    'HackSoft': 'https://hacksoft.io',
    'HackBulgaria': 'https://hackbulgaria.com',
    'HackConf': 'https://hackconf.bg'
}

for name, url in d.items():
    print(name, url)


for a, b, c in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)


identifiers = [
    "b37fe64cd6b046d699c6aab1cb989486",
    "0016468647b84e7db9187356517c14b0",
    "1074f7a611a1475e8530c0053cd94203"
]

for index, identifier in enumerate(identifiers):
    print(index, identifier)


# x, y, z = (1, 2)  # ValueError
# x, y = (1,)  # ValueError
# x, y = (1, 2, 3)  # ValueError


# 2. While loops

index = 0
n = 4

while index < n:
    print(index)
    index = index + 1

    if index == 3:
        break
    else:
        continue


# 3. String formatting

a = "is"
b = "pretty well"

f_string = f"this string {a} formatted {b}"
format_method = "this string {a} formatted {b}".format(a=a, b=b)

print(f_string)
print(format_method)

words = ["A", "list", "of", "strings"]
print(" ".join(words))
