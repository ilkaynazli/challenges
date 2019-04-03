"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        
        def length(node):
            if not node:
                return 0
            left = length(node.left)
            right = length(node.right)
            lc = rc = 0
            
            if node.left and node.left.val == node.val:
                lc = 1 + left

            if node.right and node.right.val == node.val:
                rc = 1 + right
            
            self.res = max(self.res, lc+rc)
            return max(lc, rc)
        
        length(root)
        return self.res