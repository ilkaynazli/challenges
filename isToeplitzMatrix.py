"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        x = min(len(matrix),len(matrix[0]))
        y = max(len(matrix),len(matrix[0]))

        j = 0
        while j < y - 1:
            i = 0
            while i < len(matrix) - 1 and i + 1 + j < len(matrix[0]):
                if matrix[i][i+j] == matrix[i+1][i+1+j]:
                    i += 1
                else:
                    return False
            j += 1
        j = 1
        while j < y - 1:
            i = 0 
            while i < len(matrix[0]) - 1 and i + j < len(matrix) - 1:
                if matrix[i + j][i] == matrix[i+1+j][i+1]:
                    i += 1
                else:
                    return False 
            j += 1
        return True