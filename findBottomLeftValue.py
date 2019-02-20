"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0
        
        q = collections.deque([(root, 1)])
        res = [[root.val]]
        while q:
            cur, step = q.popleft()
            temp = []
            if cur.left:
                q.append((cur.left, step+1))
                temp.append(cur.left.val)
            if cur.right:
                q.append((cur.right, step+1))
                temp.append(cur.right.val)
            if temp:
                if len(res) > step:
                    res[step] += temp
                else:
                    res.append(temp)
        
        return res[-1][0]