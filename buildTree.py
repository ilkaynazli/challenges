"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        root = TreeNode(postorder.pop())
        index_r = inorder.index(root.val)
        left_in = inorder[:index_r]
        right_in = inorder[index_r+1:]
        if right_in:
            root.right = self.buildTree(right_in, postorder)
        if left_in:
            root.left = self.buildTree(left_in, postorder)
        
        return root
        
        