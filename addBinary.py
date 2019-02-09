"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            a, b = b, a
        
        i = len(a) - 1
        j = len(b) - 1
        rem = 0
        res = ''
        
        while i >= 0:
            total = int(a[i]) + int(b[j]) + rem
            if total >= 2:
                rem = 1
                total = total%2
            else:
                rem = 0
            res = str(total) + res
            i -= 1
            j -= 1
        
        while j >= 0:
            total = int(b[j]) + rem
            if total >= 2:
                rem = 1
                total = total%2
            else:
                rem = 0
            res = str(total) + res
            j -= 1
        
        if rem:
            res = str(rem) + res
        
        return res
        