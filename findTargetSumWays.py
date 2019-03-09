"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        res = [1*nums[0], -1*nums[0]]
        i = 1
        while i < len(nums):
            temp = []
            for num in res:
                temp.append(num + nums[i])
                temp.append(num + (-1)*nums[i])
            res = temp[::]
            i += 1
        
        return res.count(S)

# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         def summ(nums):
#             if len(nums) == 0:
#                 return []
#             if len(nums) == 1:
#                 return [nums[0], -nums[0]]
#             else:
#                 tmp = summ(nums[1:])
#             return [x+nums[0] for x in tmp] + [x-nums[0] for x in tmp]
#         return summ(nums).count(S)
            