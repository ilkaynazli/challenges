"""
    Given a string that has month and year separated by space return the number 
    of days in that month.
    assume that leap years on multiples of 4

    >>> month_to_days("11 2018")
    30
    >>> month_to_days("2 2016")
    29
    >>> month_to_days("7 1999")
    31
"""

def month_to_days(s):
    days_dict = {
                 1: 31,
                 2: 28,
                 3: 31,
                 4: 30,
                 5: 31,
                 6: 30,
                 7: 31,
                 8: 31,
                 9: 30,
                 10: 31,
                 11: 30,
                 12: 31
    }

    month_s, year_s = s.split()
    month = int(month_s)
    year = int(year_s)
    if month == 2 and year % 4 == 0:
        return 29

    return days_dict[month]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
