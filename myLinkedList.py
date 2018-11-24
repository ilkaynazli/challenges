"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        current = self.head
        while index >= 1:
            if current is None:
                return -1
            current = current.next
            index -= 1

        if current is None:
                return -1
        return current.val

        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head

        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        new_tail = Node(val)
        current = self.head
        while current:
            if current.next is None:
                current.next = new_tail
                new_tail.next = None
            current = current.next

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        count = 0
        current = self.head
        new_node = Node(val)
        if index == 0:
            self.addAtHead(val)
            return
        while count < index-1:
            if current is None:
                break
            current = current.next
            count += 1
        if current is not None:
            new_node.next = current.next
            current.next = new_node

        
    def printLL(self):
        current = self.head
        lst =[]
        while current:
            lst.append(current.val)
            current = current.next
        print(lst)
            
            

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        current = self.head
        while index > 1:
            if current is None:
                break
            current = current.next
            index -= 1
        if current is not None and current.next is not None:
            current.next = current.next.next
