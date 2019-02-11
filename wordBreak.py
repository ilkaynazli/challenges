"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution:    
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        
        def wordB2(s, wordDict, helper):
            
            if s in wordDict:
                return True
            if not s:
                return True

            if s in helper:
                return helper[s]

            i = 0
            while i < len(s) - 1:
                if s[:i+1] in wordDict:
                    temp = wordB2(s[i+1:], wordDict, helper)
                    helper[s[i+1:]] = temp
                    if temp:
                        return True
                i += 1
            helper[s] = False
            return False
        
        helper = {}
        return wordB2(s, wordDict, helper)