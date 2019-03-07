"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                new.append(nums2[j])
                j += 1
            else:
                new.append(nums1[i])
                i += 1
        while i < len(nums1):
            new.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            new.append(nums2[j])
            j += 1
        print(new)
        n = len(new)
        if n % 2 == 0:
            return (new[n//2] + new[n//2-1])/2
        return new[n//2] * 1.0
        
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n 
        
        imin = 0 
        imax = n
        half = (m + n + 1)//2
        while imin <= imax:
            i = (imin + imax) //2
            j = half - i
            if i < n and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])
                
                if (m+n) % 2 == 1:
                    return max_left
                
                if i == n:
                    min_right = nums2[j]
                elif j == m:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                
                return (max_left + min_right) / 2.0
"""