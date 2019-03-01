"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        directions = {(1,0), (-1,0), (0,1), (0,-1)}
        n = len(matrix)
        m = len(matrix[0])
        queue = collections.deque()
        
        res = []
        for r in range(n):
            temp = []
            for c in range(m):
                temp.append(math.inf)
            res.append(temp)
            
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    res[r][c] = 0
                    queue.append((r,c))
        while queue:
            row, col = queue.popleft()
            for d in directions:
                r = row + d[0]
                c = col + d[1]
                if r < 0 or c < 0 or r >= n or c >= m:
                    continue
                if res[r][c] > (res[row][col] + 1):
                    res[r][c] = res[row][col] + 1
                    queue.append((r,c))
        return res