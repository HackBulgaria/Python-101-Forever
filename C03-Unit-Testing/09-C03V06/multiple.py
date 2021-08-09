# multiple.py

def fail(exception_cls):
    raise exception_cls("Ooops")


try:
    fail(ValueError)
except Exception as exc:
    print("Can catch ValueError as Exception.")
    print(exc.__class__)
except ValueError as exc:
    print("Can catch ValueError as ValueError.")
    print(exc.__class__)


try:
    fail(ValueError)
except ValueError as exc:
    print("Can catch ValueError as ValueError.")
    print(exc.__class__)
except Exception as exc:
    print("Can catch ValueError as Exception.")
    print(exc.__class__)


try:
    fail(ValueError)
except (ValueError, Exception) as exc:
    print("Can catch multiple exceptions in a single except block")
    print(exc.__class__)
