"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            if self.right:
                right = heapq.heappop(self.right)
                if right <= num:
                    heapq.heappush(self.left, -1 * right)
                    heapq.heappush(self.right, num)
                else:
                    heapq.heappush(self.left, -1 * num)
                    heapq.heappush(self.right, right)
            else:
                heapq.heappush(self.left, -1 * num)
             
        elif len(self.left) > len(self.right):
            left = heapq.heappop(self.left)
            if -1 * left >= num:
                heapq.heappush(self.left, -1 * num)
                heapq.heappush(self.right, -1 * left)
            else:
                heapq.heappush(self.right, num)
                heapq.heappush(self.left, left)
            

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            left = heapq.heappop(self.left)
            right = heapq.heappop(self.right)
            
            heapq.heappush(self.left, left)
            heapq.heappush(self.right, right)
            return (-1*left + right) / 2.0
        
        left = heapq.heappop(self.left)
        heapq.heappush(self.left, left)
        return -1.0 * left


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()