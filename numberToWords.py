"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def one(num): 
            digits = {1:'one',
                    2:'two',
                    3:'three',
                    4:'four',
                    5:'five',
                    6:'six',
                    7:'seven',
                    8:'eight',
                    9:'nine'}
            return digits.get(num)
        
        def ten_to_19(num):
            digits = {10: 'ten', 
                     11:'eleven',
                     12: 'twelve',
                     13: 'thirteen',
                     14: 'fourteen',
                     15: 'fifteen',
                     16: 'sixteen',
                     17: 'seventeen',
                     18: 'eighteen',
                     19: 'nineteen'}
            return digits.get(num)
        
        def tens(num):
            digits = {2: 'twenty',
                     3: 'thirty',
                     4: 'forty',
                     5: 'fifty',
                     6: 'sixty',
                     7: 'seventy',
                     8: 'eighty',
                     9: 'ninety'}
            return digits.get(num)
        
        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return ten_to_19(num)
            else:
                tenner = num//10
                rest = num - tenner * 10
                return tens(tenner) + ' ' + one(rest) if rest else tens(tenner)                        
        
        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + ' hundred ' + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' hundred'
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        if not num:
            return 'Zero'
        
        result = ''
        if billion:
            result = three(billion) + ' billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        
        return result.title()