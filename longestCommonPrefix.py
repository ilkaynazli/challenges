"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def helper(s1, s2):
            if len(s1) > len(s2):
                s1, s2 = s2, s1
                
            i = 0
            ans = ''
            while i < len(s1):
                if s1[i] == s2[i]:
                    ans += s1[i]
                else:
                    break
                i += 1
            return ans
            
        if not strs:
            return ''
        
        res = strs[0]
        n = len(strs)
        i = 1
        while i < n:
            temp = helper(res, strs[i])
            res = temp
            i += 1
        return res
        