"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        remainder = 0
        first = None
        prev = None
        while l1 or l2 or remainder:
            total = 0
            if l1:
                total += l1.val
            if l2:
                total += l2.val
            total += remainder
            
            if total >= 10:
                remainder = 1
                sum_num = total % 10
            else:
                sum_num = total
                remainder = 0
                
            new_node = ListNode(sum_num)  
            if first is None:
                first = new_node
            if prev:
                prev.next = new_node
            prev = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return first