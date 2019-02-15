"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if head is None:
            return None
        if head.next is None:
            return head
        
        new_head = head
        
        while head.next:
            temp = head.next
            head.next = temp.next
            temp.next = new_head
            new_head = temp
        
        return new_head
        
        