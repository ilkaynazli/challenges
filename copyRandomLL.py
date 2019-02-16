"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        copy = RandomListNode(0)
        first = copy
        
        current = head
        while current:
            copy.next = RandomListNode(current.label)
            copy = copy.next
            if current.random:
                copy.random = RandomListNode(current.random.label)
            else:
                copy.random = None
            
            current = current.next
        
        return first.next