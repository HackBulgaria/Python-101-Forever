import traceback


def a():
    b()


def b():
    c()


def c():
    print_callstack()


def print_callstack():
    for line in traceback.format_stack():
        print(line.strip())


def main():
    a()
    print("----------------")
    print_callstack()


main()
