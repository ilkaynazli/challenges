"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 1:
            return nums
        n = len(nums)
        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[-1] = nums[-1]
        
        for i in range(1, n):
            if i%k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])
            j = n - i - 1
            if (j+1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])
        
        res = []
        for i in range(n-k+1):
            res.append(max(left[i+k-1], right[i]))
        
        return res

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if not nums:
#             return []
#         if k == 1:
#             return nums
        
#         def clean_deque(i):
#             if q and q[0] == i-k:
#                 q.popleft()
#             while q and nums[i] > nums[q[-1]]:
#                 q.pop()
 
#         output = []
#         max_id = 0
#         q = collections.deque()
#         for i in range(k):
#             clean_deque(i)
#             q.append(i)
#             if nums[i] > nums[max_id]:
#                 max_id = i
#         output = [nums[max_id]]
        
#         for i in range(k, len(nums)):
#             clean_deque(i)
#             q.append(i)
#             output.append(nums[q[0]])
            
#         return output


# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if not nums:
#             return []
        
#         output = []
#         q = collections.deque(nums[:k])
#         while q:
#             output.append(max(q))
#             q.popleft()
#             if k < len(nums):
#                 q.append(nums[k])
#                 k += 1
#             else:
#                 break
        
#         return output