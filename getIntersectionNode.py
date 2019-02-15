"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def length(head):
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count
        
        lA = length(headA)
        lB = length(headB)
        if lA > lB:
            headA, headB = headB, headA
        
        dif = abs(lA - lB)
        
        currentB = headB
        while dif > 0:
            currentB = currentB.next
            dif -= 1
        
        currentA = headA
        while currentA and currentB:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next
            
        return None



# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         llA_set = set()
#         if headA is None:
#             return None
#         current = headA
#         while current:
#             llA_set.add(current)
#             current = current.next
#         currentB = headB
#         while currentB:
#             if currentB in llA_set:
#                 return currentB
#             currentB = currentB.next
            
#         return None
#             