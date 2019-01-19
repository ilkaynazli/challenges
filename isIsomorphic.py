"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        
        for i, char in enumerate(s):
            if char in s_dict:
                s_dict[char].append(i)
            else:
                s_dict[char] = [i]
        
        for i, char in enumerate(t):
            if char in t_dict:
                t_dict[char].append(i)
            else:
                t_dict[char] = [i]
        # print(s_dict, t_dict)
        
        value_s = []
        for value in s_dict.values():
            value_s.append(value)
        value_t = []
        for value in t_dict.values():
            value_t.append(value)
        
        # print(value_s, value_t)
        value_s.sort()
        value_t.sort()
        if len(value_s) == len(value_t):
            i = 0
            while i < len(value_s):
                if value_s[i] == value_t[i]:
                    i += 1
                else:
                    return False
            return True
        else:
            return False