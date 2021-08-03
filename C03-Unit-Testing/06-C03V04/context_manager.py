# context_manager.py
class EchoManager:
    def __enter__(self):
        print("enter")

        context_manager_value = 42

        return context_manager_value

    def __exit__(self, exception_type, exception_value, exception_traceback):
        print("exit")

        # If no exception, None, None, None
        print(exception_type, exception_value, exception_traceback)


with EchoManager() as value:
    print(value)  # 42
