"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        if len(set(s)) <= 2:
            return len(s)
        c = {}
        l = 0
        r = 0
        ans = 0
        while r < len(s):
            char = s[r]
            if len(c) < 3:
                c[char] = r
                r += 1
            if len(c) == 3:
                del_idx = min(c.values())
                del c[s[del_idx]]
                l = del_idx + 1
            ans = max(ans, r - l)

        return ans

# class Solution:
#     def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
#         if not s:
#             return 0
#         if len(set(s)) <= 2:
#             return len(s)
#         c = {}
#         l = 0
#         r = 0
#         ans = 0
#         while r < len(s):
#             char = s[r]
#             c[char] = c.get(char, 0) + 1
#             if len(c) > 2:
#                 ans = max(ans, r - l)
#                 c = {}
#                 l += 1
#                 r = l
#                 continue
#             r += 1
#         if len(c) <= 2:
#             ans = max(ans, r-l)
#         return ans
            
        
