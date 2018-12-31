"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        my_dict = {}
        for char in s:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        for char in t:
            if char in my_dict:
                my_dict[char] -= 1
            else:
                return False
        for value in my_dict.values():
            if value is not 0:
                return False
        return True
        
        """
        #using collections.Counter()

        import collections
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        return c1 == c2

        """
        
                
            