"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
#solution 1

class Solution:    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype:  List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        
        my_list = self.generate(numRows - 1)
        prev = my_list[-1]
        i = 0
        lst = [1]
        while i < len(prev) - 1:
            lst.append(prev[i] + prev[i+1])
            i += 1
        lst.append(1)
        my_list.append(lst)
        return my_list 
        
#solution 2

class Solution:
    check_list = {}
    
    def generate_helper(self, numRows):
        """
        :type numRows: int
        :rtype: List[int]
        """
        if numRows in self.check_list:
            return self.check_list[numRows]

        if numRows == 1:
            self.check_list[numRows] = [1]
            return [1]
        
        prev = self.generate_helper(numRows - 1)
        i = 0
        lst = [1]
        while i < len(prev) - 1:
            lst.append(prev[i] + prev[i+1])
            i += 1
        lst.append(1)
        self.check_list[numRows] = lst
        return lst
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        new_list = []
        i = 1
        while i <= numRows:
            new_list.append(self.generate_helper(i))
            i += 1
            # print(str(new_list))
        return new_list
        