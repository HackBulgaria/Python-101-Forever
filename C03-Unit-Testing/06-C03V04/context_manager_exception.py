# context_manager_exception.py

class EchoManager:
    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception_value, exception_traceback):
        #     ValueError    , str(exception) , traceback_object
        # <class 'ValueError'> OOOPS <traceback object at 0x7f47175d7200>
        print(exception_type, exception_value, exception_traceback)

        return True


with EchoManager():
    raise ValueError("OOOPS")
