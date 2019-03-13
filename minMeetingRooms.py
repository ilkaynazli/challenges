"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        
        stack = []
        temp = []
        for interval in intervals:
            if stack and stack[-1] <= interval.start:
                stack.pop()
            while stack and stack[-1] < interval.end:
                temp.append(stack.pop())
            stack.append(interval.end)
            while temp:
                stack.append(temp.pop())
            
        return len(stack)