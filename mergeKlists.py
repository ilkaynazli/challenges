"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        head = cur = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
                
        while q:
            val, node = q.get()
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                q.put((node.val, node))
                
        return head.next