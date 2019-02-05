"""Translate phrase to "leet-speak".

For example::

    >>> translate_leet("Hi Balloonicorn")
    'Hi B@1100nic0rn'

    >>> translate_leet("Hackbright is the Shizzle")
    'H@ckbrigh7 i5 7h3 5hizz13'

"""


def translate_leet(phrase):
    """Translates input into "leet-speak"."""
    key = {'a': '@',
           'o': '0',
           'e': '3',
           'l': '1',
           's': '5',
           't': '7',
           'A': '@',
           'O': '0',
           'L': 'l',
           'E': '3',
           'S': '5',
           'T': '7'}
    s = ''

    for char in phrase:
        if char in key:
            s += key[char]
        else:
            s += char

    return s


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AE3S0M3!\n")
