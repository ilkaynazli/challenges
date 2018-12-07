"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        i = 0
        seen = set()
        while i < len(s):
            if s[i] in seen:
                i += 1
                continue
            if s[i] not in s[i+1:]:
                return i
            else:
                seen.add(s[i])
            i += 1
        return -1