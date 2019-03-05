"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
 B B
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        q = collections.deque([root])
        seen = set()
        while q:
            cur = q.popleft()
            if k - cur.val in seen:
                return True
            else:
                seen.add(cur.val)
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        
        return False