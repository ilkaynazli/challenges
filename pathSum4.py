"""
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:
The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.

Example 1:
Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
Example 2:
Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.ans = 0
        root = Node(nums[0] % 10)
        
        for i in range(1, len(nums)):
            D, P, V = nums[i] // 100, nums[i] // 10 % 10, nums[i] % 10
            P -= 1
            cur = root
            for d in range(D-2, -1, -1):
                if P < 2**d:
                    cur.left = cur = cur.left or Node(V)
                else:
                    cur.right = cur = cur.right or Node(V)
                P %= 2**d
        
        def traverse(node, cur_sum=0):
            if not node:
                return
            cur_sum += node.val
            if not node.left and not node.right:
                self.ans += cur_sum
            else:
                traverse(node.left, cur_sum)
                traverse(node.right, cur_sum)
        
        traverse(root)
        return self.ans