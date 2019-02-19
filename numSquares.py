"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        
        lst = []
        i = 1
        while i*i <= n:
            lst.append(i*i)
            i += 1
        
        to_visit = {n}
        count = 0
        while to_visit:
            count += 1
            temp = set()
            for i in to_visit:
                for j in lst:
                    if i == j:
                        return count
                    if i < j:
                        break
                    temp.add(i-j)
            to_visit = temp
        