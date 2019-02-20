"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
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
                    
        ans = []
        for item in res:
            ans.append(sum(item)/len(item))
            
        return ans