"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        while num > 9:
            result += num % 10
            num = num // 10
        result += num
        if result > 9:
            return self.addDigits(result)
        else:
            return result