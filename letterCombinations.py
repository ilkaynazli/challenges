"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        key = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        
        if len(digits) == 0:
            return []
        
        temp = key[digits[0]]
        temp2 = []
        i = 1
        while i < len(digits):
            j = 0
            while j < len(key[digits[i]]):
                k = 0
                while k < len(temp):
                    temp2.append(temp[k] + key[digits[i]][j])
                    k += 1
                j += 1
            temp = temp2[:]
            temp2 = []
            i += 1

        return temp