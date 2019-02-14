"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        if head is None:
            return None
        
        before = ListNode(None)
        after = ListNode(None)
        current = head
        while current:
            if current.val < x:
                if before.val is None:
                    bhead = ListNode(current.val)
                    bhead.next = None
                    before = bhead
                else:
                    before.next = ListNode(current.val)
                    before = before.next
            else:
                if after.val is None:
                    ahead = ListNode(current.val)
                    ahead.next = None
                    after = ahead
                else:
                    after.next = ListNode(current.val)
                    after = after.next
            current = current.next
        
        after.next = None
        if before.val is None:
            return ahead
        if after.val is None:
            return bhead
        before.next = ahead
        return bhead
        
        