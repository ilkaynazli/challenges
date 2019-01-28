"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        
        product = 1
        i = 0
        while i < len(nums):
            res[i] *= product
            product *= nums[i]
            i += 1
        
        # print(res)
        
        product = 1
        i = len(nums) - 1
        while i >= 0:
            res[i] *= product
            product *= nums[i]
            i -= 1
        
        # print(res)
        
        return res
            

# class Solution(object):
#     def helper(self, arr):
#         product = 1
#         for num in arr:
#             product *= num
#         return product
    
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         res = []
#         i = 0
#         while i < len(nums):
#             res.append(self.helper(nums[:i] + nums[i+1:]))
#             i += 1
            
#         return res