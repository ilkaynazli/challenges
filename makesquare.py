"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
"""

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        summ = sum(nums)
        side = summ // 4
        if side * 4 != summ:
            return False

        n = len(nums)
        cache = {}
        
        def helper(mask, sides_done):
            total = 0
            for i in range(n-1, -1, -1):
                if not (mask & 1 << i):
                    total += nums[n - 1 - i]
            if total > 0 and total % side == 0:
                sides_done += 1
            if sides_done == 3:
                return True
            if (mask, sides_done) in cache:
                return cache[(mask, sides_done)]
            ans = False
            c = total // side
            rem = side * (c+1) - total
            for i in range(n-1, -1, -1):
                if nums[n-1-i] <= rem and mask&(1 << i):
                    if helper(mask ^ (1 << i), sides_done):
                        ans = True
                        break
            cache[(mask, sides_done)] = ans
            return ans
        return helper((1<<n) - 1, 0)


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        summ = sum(nums)
        side = summ // 4
        if side * 4 != summ:
            return False
        
        nums.sort(reverse=True)
        
        sums = [0 for x in range(4)]
        
        def dfs(idx):
            if idx == len(nums):
                return sums[0] == sums[1] == sums[2] == side
            for i in range(4):
                if sums[i] + nums[idx] <= side:
                    sums[i] += nums[idx]
                    if dfs(idx+1):
                        return True
                    sums[i] -= nums[idx]
            return False
        
        return dfs(0)