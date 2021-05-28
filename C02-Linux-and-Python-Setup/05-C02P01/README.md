# C02P01 - Reduce file path

A file path in a Unix-like operating system looks like this:

```
/home/user/courses/Programming101-Python/week01
```

We start from the root - `/` and we navigate to the destination folder.

But there is a problem - if we have `..` and `.` in our file path, it's not clear where we are going to end up.

-   `..` means to go back one directory.
-   `.` means to stay in the same directory.
-   we can have more then one `/` between the directories - `/home//code`.

So for example: 

```
/home//user/courses/./Programming101-Python/week01/../
```

reduces to

```
/home/user/courses/Programming101-Python
```

Implement a function, called `reduce_file_path(path)` which takes a string and returns the reduced version of the path.

-   Every `..` means that we have to go one directory back.
-   Every `.` means that we are staying in the same directory.
-   Every extra `/` is unnecessary.
-   Always remove the last `/`.

**Avoid using a standard library for dealing with Unix paths.**

## Signature

```python
def reduce_file_path(path):
    pass
```

## Examples

```python
reduce_file_path("/") == "/"
reduce_file_path("/srv/../") == "/"
reduce_file_path("/srv/www/htdocs/wtf/") == "/srv/www/htdocs/wtf"
reduce_file_path("/srv/www/htdocs/wtf") == "/srv/www/htdocs/wtf"
reduce_file_path("/srv/./././././") == "/srv"
reduce_file_path("/etc//wtf/") == "/etc/wtf"
reduce_file_path("/etc/../etc/../etc/../") == "/"
reduce_file_path("//////////////") == "/"
reduce_file_path("/../") == "/"
```
