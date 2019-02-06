"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2
"""


def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""
    words_d = {}
    for word in phrase.split():
        if word in words_d:
            words_d[word] += 1
        else:
            words_d[word] = 1

    res = []
    for k,v in sorted(words_d.items(), key=lambda word: word[1]):
        res.append((k, v))

    res.sort()
    
    for k,v in res:
        print(k + ':', v)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
