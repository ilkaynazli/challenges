"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        
        max_up_to = [0] * n
        max_up_to[0] = nums[0]
        
        min_up_to = [0] * n
        min_up_to[0] = nums[0]
        
        for i in range(1, n):
            max_up_to[i] = max(max_up_to[i-1] * nums[i],
                               min_up_to[i-1] * nums[i],
                               nums[i])
            min_up_to[i] = min(max_up_to[i-1] * nums[i],
                               min_up_to[i-1] * nums[i],
                               nums[i])
        return max(max_up_to)