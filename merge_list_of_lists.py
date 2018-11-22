"""
    Given a list of sorted lists of integers, return one sorted list containing 
    all values

    >>> lst = [[1,2,4], [3], [7,10]]
    >>> sorted_lists(lst)
    [1, 2, 3, 4, 7, 10]
"""

def sorted_lists(lsts):

    def merge(lst1, lst2):
        new_list = []
        while len(lst1) > 0 or len(lst2) > 0:
            if lst1 == []:
                new_list.extend(lst2)
                break
            if lst2 == []:
                new_list.extend(lst1)
                break
            if lst1[0] < lst2[0]:
                new_list.append(lst1.pop(0))
            else:
                new_list.append(lst2.pop(0))
        return new_list

    if lsts == []:
        return []
    if len(lsts) == 1:
        return lsts[0]

    m = merge(lsts[0], lsts[1])
    lsts = [m] + lsts[2:]
    return sorted_lists(lsts)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
