"""
Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.
 
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: 'int') -> 'Node':
        new = Node(insertVal, None)
        def insert_node(cur, new):
            new.next = cur.next
            cur.next = new
            
        if head is None:
            head = new
            return head
            
        current = head
        while current:
            if (current.val < new.val and current.next.val >= new.val):
                insert_node(current, new)
                break
            if current.next.val < current.val:
                if current.next.val >= new.val or current.val < new.val:
                    insert_node(current, new)
                    break
            current = current.next
            if current.next == head:
                insert_node(current, new)
                break
        
        return head