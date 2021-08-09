def fail():
    raise Exception("Ooops")


def main():
    fail()
    print("We will never reach here")


try:
    main()
except Exception as exc:
    print("Some kind of exception happened")
    print(exc)
