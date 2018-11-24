"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            current = head
            while current.next.next:
                current = current.next
            new_node = current.next
            current.next = None
            new_list = new_node
            new_node.next = self.reverseList(head)
            return new_node
            

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head is None:
#             return None
#         elif head.next is None:
#             return head
#         else:
#             current = head
#             new_one = None
#             second = None
            
#             while current:
#                 second = current.next
#                 current.next = new_one
#                 new_one = current
#                 current = second

#             return new_one