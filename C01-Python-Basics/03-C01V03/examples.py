if True:
    pass


if False:
    pass


expression = (2 + 1) * 5


# Implicit conversion
# if bool(expression):
if expression:
    pass


if expression == 123:
    pass


if expression is True:
    pass


a_boolean = True


if a_boolean:
    pass


# More explicit way
if a_boolean is True:
    pass


# null value
a_null = None


if a_null:
    pass


if not a_null:
    pass


# More explicit way
if a_null is None:
    pass


# More explicit way
if a_null is not None:
    pass


# Falsy values

if []:
    pass


if {}:
    pass


if 0:
    pass
else:
    pass


if '':
    pass


today = 'Monday'
hour = '15:00'


if today == 'Monday':
    pass
elif today == 'Tuesday':
    pass
elif today == 'Wednesday':
    pass
else:
    pass


if today == 'Monday':
    if hour == '15:00':
        pass
    else:
        pass
else:
    pass
