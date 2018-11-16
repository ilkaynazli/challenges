"""Return maximum profit possible for buying-and-selling a stock.

The `best` function will be given a list of stock prices as they
happened throughout the day::

    best([15, 10, 20, 22, 1, 9])

It should return the maximum possible profit on the stock for that day.
For example, with these prices, our best option would have been to
buy the stock at $10 and sell it at $22. So the profit would be $12::

    >>> best([15, 10, 20, 22, 1, 9])
    12

Best profit: $4 (buy at $1, sell at $5)::

    >>> best([1, 2, 3, 4, 5])
    4

Other tests:

    >>> best([2, 3, 10, 6, 4, 8, 1])
    8

    >>> best([7, 9, 5, 6, 3, 2])
    2

    >>> best([0, 100])
    100

Io profit is possible, so return $0::

    >>> best([5,4 ,3, 2, 1])
    0

    >>> best([100])
    0

    >>> best([100, 0])
    0



"""


def best(prices):
    """"Given a list of prices, return the maximum profit.

    If no profit is possible, return 0.
    """
    # keep = 0
    # i=0
    # while i < len(prices):
    #     first = prices[i]
    #     for j in range(i+1, len(prices)):
    #         check = prices[j] - first
    #         if check >= keep:
    #             keep = check
    #         if check < 0:
    #             check = 0
    #             i = j
    #             break
    #     i += 1

    # return keep

    """"Given a list of prices, return the maximum profit.

    If no profit is possible, return 0.
    """

    # START SOLUTION

    max_diff = 0
    low_so_far = None

    for p in prices:

        if low_so_far is None or p < low_so_far:
            low_so_far = p

        diff = p - low_so_far

        if diff > max_diff:
            max_diff = diff

    return max_diff



if __name__ == '__main__':
    import doctest

    print()
    if doctest.testmod().failed == 0:
        print("\t*** ALL TESTS PASSED; YOU CAN TAKE THAT TO THE BANK!")
    print()
