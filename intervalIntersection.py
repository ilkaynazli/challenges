"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        if not A or not B:
            return []
        if A[0].start > B[0].start:
            A, B = B, A
        res = []
        i = 0
        j = 0
        n = len(A)
        m = len(B)
        while i < n and j < m:
            low = max(A[i].start, B[j].start)
            high = min(A[i].end, B[j].end)
            if low <= high:
                res.append(Interval(low, high))
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1
                
        return res
            
