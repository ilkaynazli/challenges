"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True
        for x in (2,3,5):
            while num % x == 0:
                num = num / x
        return num == 1
    
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = None
        test = 1
        while n > 0:
            if self.isUgly(test):
                result = test
                n -= 1
            test += 1
            
        return result