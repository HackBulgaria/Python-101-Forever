def a():
    b()


def b():
    fail()


def fail():
    raise Exception("Ooops")
    c()


def c():
    print("We will never reach here")


def main():
    a()
    print("We will never reach here")


main()
