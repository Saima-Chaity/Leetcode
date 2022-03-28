# Moving Average from Data Stream - https://leetcode.com/problems/moving-average-from-data-stream/

'''Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3'''

from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.sum = 0
        self.length = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        self.length += 1
        total = self.sum / self.length
        if self.length == self.size:
            self.sum -= self.q.popleft()
            self.length -= 1
        return total


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)