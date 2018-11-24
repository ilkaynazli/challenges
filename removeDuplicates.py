"""Given a list remove duplicates without using a set

    >>> lst = [1,2,3,4,5,5,2,3]
    >>> remove_duplicates(lst)
    [1, 2, 3, 4, 5]

"""

def remove_duplicates(lst):
    new_list = []
    for num in lst:
        if num in new_list:
            continue
        else:
            new_list.append(num)

    return new_list

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
