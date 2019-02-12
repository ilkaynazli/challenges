"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        res = []
        if not matrix:
            return res
        
        m = len(matrix)
        n = len(matrix[0])
        seen = set()
        i = 0
        j = 0
        start = 0
        while i < m and j < n:
            if (i,j) not in seen:
                res.append(matrix[i][j])
            seen.add((i,j))
            while j < n-1:
                j += 1
                if (i,j) not in seen:
                    res.append(matrix[i][j])
                seen.add((i,j))
           
            while i < m-1:
                i += 1
                if (i,j) not in seen:
                    res.append(matrix[i][j])
                seen.add((i,j))
              
            while j > start:
                j -= 1
                if (i,j) not in seen:
                    res.append(matrix[i][j])
                seen.add((i,j))
            
            while i > start+1:
                i -= 1
                if (i,j) not in seen:
                    res.append(matrix[i][j])
                seen.add((i,j))
            
            j += 1
            m -= 1
            n -= 1
            start += 1
        
        return res
            