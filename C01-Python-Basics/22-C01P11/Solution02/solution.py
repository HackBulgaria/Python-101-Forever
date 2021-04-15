# Video - https://youtu.be/uuCIerDdLgQ

from itertools import permutations


def anagrams(word1, word2):
    # Chaining
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')

    for permutation in permutations(word1):
        w = ''.join(permutation)

        if w == word2:
            return True

    return False


tests = [
    (("silent", "listen"), True),
    (("SILENT", "listen"), True),
    (("silent", "LISTEN"), True),
    (("python", "ruby"), False),
    (("a gentleman", "elegant man"), True),
    (("eleven plus two", "twelve plus one"), True),
    (("William Shakespeare", "I am a weakish speller"), True),
    (("", ""), True)
]


for args, expected in tests:
    result = anagrams(*args)

    print(result == expected)
