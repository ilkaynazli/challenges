"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        pre_idx = 0
        
        def helper(left=0, right=len(inorder)):
            nonlocal pre_idx
            if left == right:
                return None
            
            root = TreeNode(preorder[pre_idx])
            ind = inorder.index(root.val)
            pre_idx += 1
            root.left = helper(left, ind)
            root.right = helper(ind+1, right)
            return root
            
        return helper()

    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     if not inorder:
    #         return None
       
    #     def helper(post=preorder[::-1], inorder=inorder):
    #         if not inorder:
    #             return None
    #         root = TreeNode(post.pop())
    #         idx = inorder.index(root.val)
    #         root.left = helper(post, inorder[:idx])
    #         root.right = helper(post, inorder[idx+1:])
    #         return root
            
    #     return helper()