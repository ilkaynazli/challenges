"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)


    def pop(self):
        """
        :rtype: int
        """
        return self.data.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        maxx = self.data[0]
        for num in self.data:
            if num > maxx:
                maxx = num
        return maxx
        

    def popMax(self):
        """
        :rtype: int
        """
        maxx = (self.data[0], 0)
        for i, num in enumerate(self.data):
        
            if num >= maxx[0]:
                maxx = (num, i)
        rem = maxx[0]
        index = maxx[1]
        self.data = self.data[:index] + self.data[index+1:]
        
        return rem      
