# https://youtu.be/Ogm9lgW-nuw
from collections import deque


def reduce_file_path(path):
    result = deque()

    for i in path.split('/'):
        if i == '..' and len(result) > 0:
            result.pop()
        if i not in ('.', '..', ''):
            result.append(i)
    return '/' + '/'.join(result)


result = [
    reduce_file_path(
        '/home//user/courses/./Programming101-Python/week01/../'
    ) == '/home/user/courses/Programming101-Python',
    reduce_file_path('/') == '/',
    reduce_file_path('/srv/../') == '/',
    reduce_file_path('/srv/www/htdocs/wtf/') == '/srv/www/htdocs/wtf',
    reduce_file_path('/srv/www/htdocs/wtf') == '/srv/www/htdocs/wtf',
    reduce_file_path('/srv/./././././') == '/srv',
    reduce_file_path('/etc//wtf/') == '/etc/wtf',
    reduce_file_path('/etc/../etc/../etc/../') == '/',
    reduce_file_path('//////////////') == '/',
    reduce_file_path('/../../../../../../../') == '/'
]
print(result)
