"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
"""

class Solution:
    def findDiagonalOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        res = []
        if not matrix:
            return res
        
        n = len(matrix)
        m = len(matrix[0])
        k = 0
        
        while k <= (m-1)+(n-1):
            if k % 2 == 0:
                i = min(k, n-1)
                j = k - i
                while i >= 0 and j <= m - 1: 
                    res.append(matrix[i][j])
                    i -= 1
                    j += 1
                    
            else:
                j = min(k, m-1)
                i = k - j
                while j >= 0 and i <= n - 1:
                    res.append(matrix[i][j])
                    i += 1
                    j -= 1
                    
            k += 1
            
        return res   