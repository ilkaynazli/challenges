"""Given a linked list, determine if it has a cycle in it."""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        current = head
        if current is None or current.next is None:
            return False
        
        while current:
            if current in visited:
                return True
            else:
                visited.add(current)
            if current.next is None:
                return False
            current = current.next

"""
        if not head or not head.next:
            return False
        pointer1 = head
        pointer2 = head.next
        
        while pointer1:
            if pointer1 is pointer2:
                return True
            if pointer2 is None or pointer2.next is None:
                return False
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
"""