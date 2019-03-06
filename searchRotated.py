"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
 
        def find_rotation(l, r):
            if nums[l] < nums[r]:
                return 0
            while l <= r:
                pivot = (r+l)//2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        r = pivot - 1
                    else:
                        l = pivot + 1
                
        def search(left, right):

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1
        
        if not nums:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        left = 0
        right = len(nums) - 1
        start = find_rotation(left, right)
        if nums[start] == target:
            return start
        if start == 0:
            return search(left, right)
        elif target >= nums[0]:
            return search(left, start - 1)
        return search(start, right)
        