"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

import collections

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter()
        
        for num in nums:
            counter[num] += 1
        most_common = counter.most_common(1)
        if most_common[0][1] > len(nums)/2:
            return most_common[0][0]