"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
    
        ans = []
        n = len(nums) 
        
        def helper(first=0):
            if first == n:
                ans.append(nums[:])
                return
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                helper(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        
        helper()
        return ans
        