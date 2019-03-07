"""
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            count = left = 0
            for right, num in enumerate(nums):
                while num - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k
        
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l

"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            return sum(prefix[min(x+guess, W)] - prefix[x] + multiplicity[i] for i, x in enumerate(nums)) >= k
        
        nums.sort()
        W = nums[-1]
        
        multiplicity = [0] * len(nums)
        
        for i, x in enumerate(nums):
            if i and x == nums[i - 1]:
                multiplicity[i] = 1 + multiplicity[i - 1]
        
        prefix = [0] * (W + 1)
        left = 0
        for i in range(len(prefix)):
            while left < len(nums) and nums[left] == i:
                left += 1
            prefix[i] = left
        
        low = 0
        high = nums[-1] - nums[0]
        while low < high:
            mid = (high + low) // 2
            if possible(mid):
                high = mid
            else:
                low = mid + 1
        return low
"""
