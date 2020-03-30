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
        self.queue = deque()

    def next(self, val: int) -> float:
        self.queue.append(val)
        average = sum(self.queue) / len(self.queue)

        if len(self.queue) == self.size:
            self.queue.popleft()
        return average

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)