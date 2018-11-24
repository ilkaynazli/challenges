"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        new_head = ListNode(val+1)
        new_head.next = head
        current = new_head
        
        while current:
            if current.next is None:     
                break
            if current.next.val == val:
                current.next = current.next.next
                continue
            current = current.next
  
        
        return new_head.next
