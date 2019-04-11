"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""

class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k
        self.heap = []
        self.res = None
        for num in self.nums:
            heapq.heappush(self.heap, (-1 * num))

        
    def find_max_k(self):
        n = self.k
        temp = []
        while n > 1:
            temp.append(heapq.heappop(self.heap))
            n -= 1        
        target = heapq.heappop(self.heap)
        heapq.heappush(self.heap, target)
        while temp:
            heapq.heappush(self.heap, temp.pop())
        return -1 * target

    
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        heapq.heappush(self.heap, -1 * val)
        if not self.res or self.res < val:
            self.res = self.find_max_k()
        return self.res
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)