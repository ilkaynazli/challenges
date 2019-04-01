"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        set_nums = set(nums)
        if len(set_nums) == 1 and set_nums.pop() == 0:
            return [[0,0,0]]
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n):
            j = i + 1
            k = n - 1
            target = -1 * nums[i]
            while j < k:
                # print(i, j, k, target, nums[j], nums[k])
                if nums[j] + nums[k] == target:
                    temp = [-target, nums[j], nums[k]]
                    s = str(temp[0]) + ',' + str(temp[1]) +' ,' + str(temp[2])
                    res.add(s)
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        ans = []
        for s in res:
            ans.append([int(x) for x in s.split(',')])
        return ans