"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x > arr[-1]:
            return arr[-k:]
        if x < arr[0]:
            return arr[:k]
        
        def find_x():
            l = 0
            r = len(arr) - 1
            while l < r:
                mid = (r+l)//2
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
            
        index = find_x()
        low = max(0, index - (k-1))
        high = min(len(arr)-1, index + (k-1))
        while low+k-1 < high:
            if low < 0 or x - arr[low] <= arr[high] - x:
                high -= 1
            elif high > len(arr) or x - arr[low] > arr[high] - x:
                low += 1     
        return arr[low:high+1]