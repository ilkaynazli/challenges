"""
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        
        q = collections.deque([(root, 1)])
        res = [[root.val]]
        
        while q:
            cur, step = q.popleft()
            
            children = [cur.left, cur.right]
            temp = []
            for child in children:
                if child:
                    q.append((child, step+1))
                    temp.append(child.val)
            if temp:
                if len(res) > step:
                    res[step] += temp
                else:
                    res.append(temp)
        
        ans = []
        for item in res:
            ans.append(max(item))
            
        return ans