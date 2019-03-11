"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if not head.next:
            return head
        temp = head.next
        head.next = head.next.next
        temp.next = head
        head = temp
        head.next.next = self.swapPairs(head.next.next)
        
        return head