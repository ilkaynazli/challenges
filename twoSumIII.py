"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}
        
        
    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

        
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        for num in self.nums:
            target = value - num
            if target in self.nums and self.nums[target] - (target is num):
                return True
  
        return False
                


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)