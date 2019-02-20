"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        if root is None:
            return []
        
        q = collections.deque([(root, 1)])
        
        res = [[root.val]]
        while q:
            cur, step = q.popleft()
            
            temp = []
            for child in cur.children:
                temp.append(child.val)
                q.append((child, step+1))
            if temp:
                if len(res) > step:
                    res[step] += temp
                else:
                    res.append(temp)
        return res