"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        p_dict = {}
        for char in p:
            if char in p_dict:
                p_dict[char] += 1
            else:
                p_dict[char] = 1
        
        result = []
        i = 0
        while i <= len(s) - len(p):
            temp = {}
            j = i
            while j < len(p) + i:
                if s[j] in temp:
                    temp[s[j]] += 1
                else:
                    temp[s[j]] = 1
                j += 1
            if temp == p_dict:
                result.append(i)
            i += 1
            
        return result