"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        def find_heights(matrix, coors):
            res = set(coors)
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            while coors:
                to_visit = []
                for row, col in coors:
                    for d in dirs:
                        r = row + d[0]
                        c = col + d[1]
                        if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or (r,c) in res:
                            continue
                        if matrix[r][c] >= matrix[row][col]:
                            res.add((r,c))
                            to_visit.append((r,c))
                coors = to_visit[:]
            return res
        
        def find_shores(matrix, pacific=True):
            res = set()
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i == 0 and pacific:
                        res.add((i,j))
                    if pacific and j == 0:
                        res.add((i,j))
                    if not pacific and j == len(matrix[0]) - 1:
                        res.add((i,j))
                    if not pacific and i == len(matrix) - 1:
                        res.add((i,j))
            return res
        
        pacific = find_shores(matrix)
        atlantic = find_shores(matrix, False)
        # print(pacific, atlantic)
        set1 = find_heights(matrix, list(pacific))
        set2 = find_heights(matrix, list(atlantic))
        # print(set1, set2)
        res = []
        for item in set1:
            if item in set2:
                res.append(item)
                
        return res
        