"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l = 1
        r = num//2
        while l <= r:
            mid = (l+r)//2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False