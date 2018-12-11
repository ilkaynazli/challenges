"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
#this solution can be faster!
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # j = 0
        # while j < len(nums) - 1:
        #     i = 0
        #     while i < len(nums)-1:
        #         if nums[i] == 0:
        #             nums[i], nums[i+1] = nums[i+1], nums[i]
        #         i += 1

        #     j += 1

        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] is not 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1