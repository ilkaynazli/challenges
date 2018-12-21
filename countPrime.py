"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution:
    def isPrime(self, num):
        if num == 2 or num == 3:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
              
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for num in range(2, n):
            if self.isPrime(num):
                count += 1
        
        return count