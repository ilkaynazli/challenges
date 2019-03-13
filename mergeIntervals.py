"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x: x.start)
        
        if intervals[1].start <= intervals[0].end <= intervals[1].end:
            low = min(intervals[0].start, intervals[1].start)
            high = max(intervals[0].end, intervals[1].end)
            res = [Interval(low, high)]
            i = 2
        else:
            res = [intervals[0]]
            i = 1

        while i < len(intervals):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(intervals[i].end, res[-1].end)
            else:
                res.append(intervals[i])
            i += 1
        return res