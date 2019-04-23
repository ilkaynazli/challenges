"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = 0
        b = 0 
        temp = 0
        
        for num in nums:
            temp ^= num
        
        mask = 1
        while not (mask & temp):
            mask <<= 1
        
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        
        return [a, b]
            