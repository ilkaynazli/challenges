"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort_s(s):
            l = list(s)
            l.sort()
            return ''.join(l)
        
        d = {}
        for s in strs:
            temp = sort_s(s)
            if temp in d:
                d[temp].append(s)
            else:
                d[temp] = [s]
        
        res = list(d.values())
        return res