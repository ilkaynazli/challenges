"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""


class Solution:    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = 0
        right = 0
        
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left == 0:
                    right += 1
                elif left > 0:
                    left -= 1
        result = {}
        
        def helper(s, idx, left_c, right_c, left_rem, right_rem, expr):
            if idx == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = ''.join(expr)
                    result[ans] = 1
            else:
                cur = s[idx]
                if (cur == '(' and left_rem > 0) or (cur == ')' and right_rem > 0):
                    helper(s, idx+1, left_c, right_c, left_rem - (cur =='('), right_rem - (cur == ')'), expr)
                expr.append(cur)
                if cur != '(' and cur != ')':
                    helper(s, idx+1, left_c, right_c, left_rem, right_rem, expr)
                elif cur == '(':
                    helper(s, idx+1, left_c+1, right_c, left_rem, right_rem, expr)
                elif cur == ')' and left_c > right_c:
                    helper(s, idx+1, left_c, right_c+1, left_rem, right_rem, expr)
                expr.pop()

        helper(s, 0, 0, 0, left, right, [])
        return list(result.keys())





# class Solution:
#     def __init__(self, valids=None, minn=None):
#         if not valids:
#             self.valid_expressions = set()
#         else:
#             self.valid_expressions = valids
#         if not minn:
#             self.min_removed = float("inf")
#         else:
#             self.min_removed = minn

        
#     def remaining(self, s, idx, left, right, expr, removed):
#         if idx == len(s):
#             if left == right:
#                 if removed <= self.min_removed:
#                     ans = ''.join(expr)
#                     if removed < self.min_removed:
#                         self.valid_expressions = set()
#                         self.min_removed = removed
#                     self.valid_expressions.add(ans)
#         else:
#             cur = s[idx]
#             if cur != '(' and cur != ')':
#                 expr.append(cur)
#                 self.remaining(s, idx+1, left, right, expr, removed)
#                 expr.pop()
#             else:
#                 self.remaining(s, idx+1, left, right, expr, removed+1)
#                 expr.append(cur)
#                 if cur == '(':
#                     self.remaining(s, idx+1, left+1, right, expr, removed)
#                 elif right < left:
#                     self.remaining(s, idx+1, left, right+1, expr, removed)
#                 expr.pop()
        
    
#     def removeInvalidParentheses(self, s: str) -> List[str]:

#         self.remaining(s, 0, 0, 0, [], 0)
#         return list(self.valid_expressions)