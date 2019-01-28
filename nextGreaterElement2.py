"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [-1] * len(nums)
        i = len(nums) - 1
        while i >= 0:
            while stack and stack[-1][1] <= nums[i]:
                stack.pop()
            if stack and nums[i] < stack[-1][1]:
                res[i] = stack[-1][1]
            stack.append((i, nums[i]))
            i -= 1

        i = len(nums) - 1
        while i >= 0:
            while stack and stack[-1][1] <= nums[i]:
                stack.pop()
            if stack and nums[i] < stack[-1][1]:
                res[i] = stack[-1][1]
            stack.append((i, nums[i]))
            i -= 1
            
        return res
    
    
#         res = [None] * len(nums)

#         i = 0
#         while i < len(nums):
#             j = i
#             while j < len(nums):
#                 if nums[i] < nums[j]:
#                     res[i] = nums[j]
#                     break
#                 j += 1
#             if res[i] is None:
#                 k = 0
#                 while k < i:
#                     if nums[i] < nums[k]:
#                         res[i] = nums[k]
#                         break
#                     k += 1
#             i += 1
#         for i in range(len(res)):
#             if res[i] == None:
#                 res[i] = -1
#         return res