"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.
"""

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        total = 0
        n = len(nums)
        counts = [0]*32
        for num in nums:
            i = 0
            while num:
                counts[i] += (num & 1)
                num >>= 1
                i += 1
        
        for count in counts:
            total += count * (n-count)
        return total
            
# class Solution:
#     def totalHammingDistance(self, nums: List[int]) -> int:
#         def count_ones(num):
#             res = 0
#             while num:
#                 res += 1
#                 num &= (num-1)
#             return res        
        
#         total = 0
#         for i, num in enumerate(nums):
#             for j in range(i+1, len(nums)):
#                 temp = num ^ nums[j]
#                 total += count_ones(temp)
#         return total
#             