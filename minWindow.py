"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        c_t = collections.Counter(t)
        required = len(c_t)
        l = r = 0
        count = 0
        window_c = {}
        ans = (math.inf, None, None)
        while r < len(s):
            char = s[r]
            window_c[char] = window_c.get(char, 0) + 1
            if char in c_t and window_c[char] == c_t[char]:
                count += 1
            
            while l <= r and count == required:
                char = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r-l+1, l, r)
                window_c[char] -= 1
                if char in c_t and window_c[char] < c_t[char]:
                    count -= 1
                l += 1
            r += 1
        return '' if ans[0] == math.inf else s[ans[1] : ans[2] + 1]
            
        
        
        return res
        