# reraising.py

def fail(exception_cls):
    raise exception_cls("Ooops")


try:
    fail(ValueError)
except Exception as exc:
    print(f"Got exception: {exc}")
    raise
