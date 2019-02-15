"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        stack = []
        slow = head
        fast = head
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast and fast.next is None:
            slow = slow.next
        
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        
        return True


# class Solution(object):
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         my_list = []
#         current = head
#         while current:
#             my_list.append(current.val)
#             current = current.next
            
#         i = 0
#         j = len(my_list)-1
#         while i < j:
#             if my_list[i] == my_list[j]:
#                 i += 1
#                 j -= 1
#             else:
#                 return False
#         return True
