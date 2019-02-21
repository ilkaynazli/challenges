"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands += 1
                    grid[i][j] = '0'
                    q = collections.deque()
                    q.append((i, j))
                    while q:
                        r, c = q.popleft()
                        
                        for d in directions:
                            k = r + d[0]
                            l = c + d[1]
                            if k >= n or k < 0 or l < 0  or l >= m:
                                continue
                            if grid[k][l] == '1':
                                q.append((k, l))
                                grid[k][l] = '0'
        
        return islands

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands += 1
                    grid[i][j] = '0'
                    q = collections.deque()
                    q.append((i, j))
                    while q:
                        r, c = q.popleft()
                        
                        for d in directions:
                            k = r + d[0]
                            l = c + d[1]
                            if k >= n or k < 0 or l < 0  or l >= m:
                                continue
                            if grid[k][l] == '1':
                                q.append((k, l))
                                grid[k][l] = '0'
        
        return islands