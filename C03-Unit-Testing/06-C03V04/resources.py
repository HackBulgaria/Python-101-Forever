# resources.py

fd = open("README.md", "r")

# Nothing stops us from getting an exception here
contents = fd.read()
print(len(contents))

# Nothing forces us to close the file,
# So we can effectively forget to do this
# And leak the file descriptor
fd.close()

# "with" statement, also known as context manager
with open("README.md", "r") as fd:
    print(len(contents))
