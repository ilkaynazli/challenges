"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if root is None:
            return []
        
        count = collections.Counter()
        res = []
        
        def dft(node):
            if node is None:
                return '#'
            s = str(node.val) + str(dft(node.left)) + str(dft(node.right))
            count[s] += 1
            if count[s] == 2:
                res.append(node)
            return s
        
        dft(root)
        
        
        return res