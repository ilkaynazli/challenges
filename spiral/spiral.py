"""Print points in matrix, going in a spiral.

Give a square matrix, like this 4 x 4 matrix, it's composed
of points that are x, y points (top-left is 0, 0):

    0,0  1,0  2,0  3,0
    0,1  1,1  2,1  3,1
    0,2  1,2  2,2  3,2
    0,3  1,3  2,3  3,3

Starting at the top left, print the x and y coordinates of each
point, continuing in a spiral.

(Since we provide 3 different versions, you can change this to
the routine you want to test:



Here are different sizes:

    >>> spiral(1)
    (0, 0)

    >>> spiral(2)
    (0, 0)
    (1, 0)
    (1, 1)
    (0, 1)

    >>> spiral(3)
    (0, 0)
    (1, 0)
    (2, 0)
    (2, 1)
    (2, 2)
    (1, 2)
    (0, 2)
    (0, 1)
    (1, 1)

    >>> spiral(4)
    (0, 0)
    (1, 0)
    (2, 0)
    (3, 0)
    (3, 1)
    (3, 2)
    (3, 3)
    (2, 3)
    (1, 3)
    (0, 3)
    (0, 2)
    (0, 1)
    (1, 1)
    (2, 1)
    (2, 2)
    (1, 2)
"""

# tuples of (x,y) 
# i need to move first x then y then x and y again
# recursion?
# print the results
# start with (0,0)
# for loops to change the x and y
# and print after each change


def spiral(matrix_size):
    """Spiral coordinates of a matrix of `matrix_size` size."""

    def helper(i, size):
        if i>size:
            return None

        n = size 
        x = i
        y = i

        print((x,y))    
        while x<n:
            x += 1
            print((x,y))
        while y<n:
            y += 1
            print((x,y))
        while x>i:
            x -=1
            print((x,y))
        while y>i+1:
            y -= 1
            print((x,y))
        i += 1

        helper(i, n-1)
    helper(0, matrix_size-1)

# n = 3
# x = 0, y = 0
# n > 0 
# (0,0)
# (1,0)
# (2,0)
# (2,1)
# (2,2)
# (1,2)
# (0,2)
# (0,1)
# n = 0 
# (0,1)







if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU MUST BE DIZZY WITH PRIDE!\n")
