"""
  Decode String
  Go to Discuss
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution:
    def decodeString(self, s: 'str') -> 'str':
        
        stack = []
        i = 0
        count = ''
        res = ''
        while i < len(s):
            # print(count, res, stack)
            if s[i].isdigit():
                count += s[i]
                if res:
                    stack.append(res)
                    res = ''
            elif s[i] == '[':
                stack.append(count)
                count = ''
            elif s[i] == ']':
                if stack[-1].isdigit():          
                    c = int(stack.pop())
                    res = c * res
                if stack and not stack[-1].isdigit():
                    temp = stack.pop()
                    res = temp + res    
            else:
                res += s[i]
            i += 1
            
        return res