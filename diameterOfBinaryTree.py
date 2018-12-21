"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        hl = self.maxDepth(root.left)
        hr = self.maxDepth(root.right)
        return max(hl, hr) + 1
    
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        to_visit = [root]
        max_diameter = 0
        while to_visit:
            current = to_visit.pop()
            max_diameter = max(max_diameter, (self.maxDepth(current.left) + self.maxDepth(current.right)))
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)
        return max_diameter
        