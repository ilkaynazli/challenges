"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        if not grid:
            return -1
        
        q = collections.deque()
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        step = 0
        while q:
            i, j, step = q.popleft()
            for d in dirs:
                k = i + d[0]
                l = j + d[1]
                if k < 0 or k >= n or l < 0 or l >= m:
                    continue
                if grid[k][l] == 1:
                    q.append((k,l, step+1))
                    grid[k][l] = 2
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return - 1
                
        return step