# hierarchy.py

def fail(exception_cls):
    raise exception_cls("Ooops")


try:
    fail(ValueError)
except Exception as exc:
    print("Can catch ValueError as Exception.")
    print(exc.__class__)


try:
    fail(Exception)
except ValueError as exc:
    print("Cannot catch Exception as ValueError.")
    print(exc.__class__)
