"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        q = collections.deque([(root, 1)])
        res = [[root.val]]
        
        while q:
            cur, step = q.popleft()
            
            temp = []
            if cur.left:
                temp.append(cur.left.val)
                q.append((cur.left, step+1))
            if cur.right:
                temp.append(cur.right.val)
                q.append((cur.right, step+1))
            if temp:
                if len(res) > step:
                    res[step] += temp
                else:
                    res.append(temp)
        
        return res[::-1]