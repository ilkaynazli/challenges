"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = len(nums)
        for i, num in enumerate(nums):
            res ^= num
            res ^= i
        return res
        
        # # nums_s = set(range(len(nums) + 1))
        # # for num in nums:
        # #     if num in nums_s:
        # #         nums_s.remove(num)
        # # return nums_s.pop()

        # #  the faster way is

        # n = len(nums)

        # return (n * (n + 1)) // 2 - sum(nums) 