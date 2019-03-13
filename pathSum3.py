"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        
        def traverse(node, sum):
            if not node:
                return
            sum -= node.val
            if sum == 0:
                self.count += 1
            traverse(node.left, sum)
            traverse(node.right, sum)
        
        to_visit = [root]
        while to_visit:
            cur = to_visit.pop()
            traverse(cur, sum)
            if cur:
                to_visit.append(cur.left)
                to_visit.append(cur.right)
        
        return self.count
               
        