"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        
        def helper(s, i , j):
            # print(s, i ,j)
            while i >= 0 and j < len(s) and s[i] == s[j]:
                j += 1
                i -= 1
            return j - i -1
        
        start = 0
        end = 0
        i = 0
        while i < len(s):
            len1 = helper(s, i, i)
            # print(len1)
            len2 = helper(s, i , i + 1)
            lenn = max(len1, len2)
            if lenn > end - start:
                start = i - (lenn - 1) // 2
                end = i + lenn // 2
            i += 1
            # print(start, end)
        return s[start: end+1]
        

        


    # def is_palindrome(self, s):
    #     i = 0
    #     j = len(s)-1
    #     while i < j:
    #         if s[i] == s[j]:
    #             i += 1
    #             j -= 1
    #         else:
    #             return False
    #     return True
    
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     pal = []
    #     i = 0
    #     while i <= len(s) - 1:
    #         j = i + 1
    #         while j <= len(s):
    #             if len(s[i:j]) == 1:
    #                 pal.append(s[i:j])
    #             elif self.is_palindrome(s[i:j]):
    #                 pal.append(s[i:j])
    #             j += 1
    #         i += 1
        
    #     maxx = ''
    #     for item in pal:
    #         if len(item) > len(maxx):
    #             maxx = item
    #     return maxx