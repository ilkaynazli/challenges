"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = [0]
        for num in nums:
            sums.append(num + sums[-1])
        
        n = len(sums)
        count = 0
        for i in range(n-1, 0, -1):
            for j in range(i):
                if sums[i] - sums[j] == k:
                    count += 1
        
        return count

        # count = 0
        # total = 0
        # sums = {0:1}
        # # print('x')
        # for i, num in enumerate(nums):
        #     total += num
        #     if total - k in sums:
        #         # print(count)
        #         count += sums[total-k]
        #         # print(count)
        #     sums[total] = sums.get(total, 0) + 1
        # # print(count)
        # return count