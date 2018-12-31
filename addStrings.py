"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # i = len(num1) - 1
        # j = len(num2) - 1
        # summ = ''
        # rem = 0
        # while i >= 0 or j >= 0:
        #     temp = rem
        #     if i >= 0:
        #         temp += int(num1[i])
        #     if j >= 0:
        #         temp += int(num2[j])
        #     if temp > 9:
        #         rem = 1
        #         summ = str(temp % 10) + summ
        #     else:
        #         rem = 0
        #         summ = str(temp) + summ
        #     i -= 1
        #     j -= 1
        # if rem == 1:
        #     summ = str(rem) + summ
        # return summ
        numbers = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9   
        }
        
        a = 0
        b = 0
        for num in num1:
            temp = numbers[num]
            a = a*10 + temp
        for num in num2:
            temp = numbers[num]
            b = b*10 + temp
        return str(a+b)
                