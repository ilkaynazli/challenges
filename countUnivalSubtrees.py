"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        
        if root is None:
            return self.count
        
        def helper(root):
            if root.left is None and root.right is None:
                self.count += 1
                return True
            
            same = True
            if root.left:
                same = helper(root.left) and same and root.left.val == root.val
            if root.right:
                same = helper(root.right) and same and root.right.val == root.val
           
            if same:
                self.count += 1
            return same
        
        helper(root)
        return self.count
        
        