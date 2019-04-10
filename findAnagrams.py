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
        n = len(p)
        m = len(s)
        if n > m:
            return []
        
        result = []
        c_p = collections.Counter(p)
        c_s = collections.Counter(s[:n])
        i = 0 
        j = n
        while j < m:
            # print(c_s, c_p, i, j)
            if c_s == c_p:
                result.append(i)
            c_s[s[i]] -= 1
            if c_s[s[i]] == 0:
                del c_s[s[i]]
            c_s[s[j]] += 1
            i += 1
            j += 1
        if c_s == c_p:
            result.append(i)
        return result

"""
class Solution:
    def helper(self, s, p, i):
        n = len(p)
        c_p = collections.Counter(p)
        c_s = collections.Counter(s[i:i+n])
        return c_s == c_p
        
    def findAnagrams(self, s, p):

        result = []
        i = 0
        while i <= len(s) - len(p):
            if self.helper(s, p ,i):
                result.append(i)
            i += 1
        return result
            
"""