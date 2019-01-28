"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxx = 0
        i = 0
        j = len(height) - 1
        while i < j:
            maxx = max(maxx, (j-i) * min(height[j], height[i]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return maxx
        """

        maxx = 0
        i = 0
        while i < len(height):
            j = len(height) - 1
            while j > i:
                maxx = max(maxx, (j-i)*min(height[j], height[i]))
                j -= 1
            i += 1
        return maxx
        """