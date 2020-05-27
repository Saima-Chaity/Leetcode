# Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/
'''Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

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
findMedian() -> 2'''

from heapq import heappush, heappop, heapify, heappushpop

class MedianFinder(object):

    def __init__(self):
        """
        initialize data structure here.
        """
        # min-heap containing the 1/2 largest elements
        self.minOfMax = []

        # max-heap containing the 1/2 smallest elements
        self.maxOfMin = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.minOfMax) == 0:
            heappush(self.minOfMax, num)
        elif len(self.maxOfMin) == 0:
            if num > self.minOfMax[0]:
                minNum = heappushpop(self.minOfMax, num)
                heappush(self.maxOfMin, -minNum)
            else:
                heappush(self.maxOfMin, -num)
        else:
            if num > - self.maxOfMin[0]:
                if len(self.maxOfMin) >= len(self.minOfMax):
                    heappush(self.minOfMax, num)
                else:
                    replaceNum = heappushpop(self.minOfMax, num)
                    heappush(self.maxOfMin, -replaceNum)
            else:
                if len(self.maxOfMin) <= len(self.minOfMax):
                    heappush(self.maxOfMin, -num)
                else:
                    replaceNum = - heappushpop(self.maxOfMin, -num)
                    heappush(self.minOfMax, replaceNum)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minOfMax) == len(self.maxOfMin):
            return ((self.minOfMax[0] - self.maxOfMin[0]) / 2)
        elif len(self.maxOfMin) > len(self.minOfMax):
            return - self.maxOfMin[0]
        else:
            return self.minOfMax[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()