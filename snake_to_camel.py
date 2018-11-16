"""
    Given a variable name in snake_case, return a string with that variable name written in camelCase.

    For example:

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'
"""
def snake_to_camel(s):
    words = s.split('_')
    camelS = words[0]
    for word in words[1:]:
        camelS += word.capitalize()

    return camelS


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
