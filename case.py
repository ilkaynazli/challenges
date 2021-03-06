"""Given a variable name in snake_case, return camelCase of name.

For example::

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

"""


def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""
    words = variable_name.split('_')
    s = words[0]
    for i in range(1, len(words)):
        s += words[i].capitalize()
    return s

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
