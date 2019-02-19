"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

class Solution:
    def wallsAndGates(self, rooms: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return 
        
        n = len(rooms)
        m = len(rooms[0])
        
        queue = collections.deque()   
        
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            i, j = queue.popleft()
            for d in directions:
                r = i + d[0]
                c = j + d[1]
                if r < 0 or c < 0 or r >= n or c >= m or rooms[r][c] != 2147483647: 
                    continue
                rooms[r][c] = rooms[i][j] + 1
                queue.append((r,c))
        