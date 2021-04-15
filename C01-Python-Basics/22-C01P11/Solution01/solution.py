# Video - https://youtu.be/wAXaJOxS-g8

def anagrams(word1, word2):
    # Chaining
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')

    return sorted(word1) == sorted(word2)


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
