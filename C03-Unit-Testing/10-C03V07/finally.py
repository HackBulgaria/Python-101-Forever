# finally.py

def fail(exception_cls):
    raise exception_cls("Ooops")


try:
    fail(ValueError)
except ValueError as exc:
    print(f"Got value error: {exc}")
finally:
    print("All is good")


try:
    print("No exception here")
except ValueError as exc:
    print(f"Got value error: {exc}")
finally:
    print("All is good")


try:
    fail(ValueError)
finally:
    print("All is good")
