"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        n = len(haystack)
        m = len(needle)
        
        if m > n:
            return -1
        if m == n:
            if haystack == needle:
                return 0
            else:
                return -1
                   
        i = 0
        while i < n:
            j = 0
            if haystack[i] == needle[j]:
                k = i + 1
                j += 1
                while j < m and k < n:
                    if haystack[k] == needle[j]:
                        j += 1
                        k += 1
                    else:
                        break
                if j == m:
                    return i
            i += 1
        
        return -1
                        
        