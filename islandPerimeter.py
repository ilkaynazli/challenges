"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        per = 0
        n = len(grid)
        m = len(grid[0])
        i = 0
        while i < n:
            j = 0
            while j < m:
                if grid[i][j] == 1:
                    if j + 1 == m:
                        per += 1
                    if j - 1 < 0:
                        per += 1
                    if i == 0: 
                        per += 1
                    if i == n-1:
                        per += 1
                    if j >= 1 and grid[i][j-1] == 0:
                        per += 1
                    if j+1 < m and grid[i][j+1] == 0:
                        per += 1
                    if i >= 1 and grid[i-1][j] == 0:
                        per += 1
                    if i + 1 < n and grid[i+1][j] == 0:
                        per += 1
                    # print(per)
                j += 1
            i += 1
        return per