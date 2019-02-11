"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

class Solution:
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':
        if s > sum(nums):
            return 0 
        
        res = len(nums)
        fast = 0
        slow = 0 
        summ = 0
        while fast < len(nums):
            # print(res, summ, fast, slow)
            summ += nums[fast]
            while summ >= s:
                res = min(res, fast - slow + 1)
                summ -= nums[slow]
                slow += 1
            fast += 1
            
        return res