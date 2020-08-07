# Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/
'''Design a class to find the kth largest element in a stream. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

KthLargest class will have a constructor which accepts an integer k and an integer array
nums, which contains initial elements from the stream. For each call to the method KthLargest.add,
return the element representing the kth largest element in the stream.

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
You may assume that nums' length ≥ k-1 and k ≥ 1.'''

import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.K = k
        self.numsList = nums
        heapq.heapify(self.numsList)
        while len(self.numsList) > self.K:
            heapq.heappop(self.numsList)

    def add(self, val: int) -> int:
        if len(self.numsList) < self.K:
            heapq.heappush(self.numsList, val)
        else:
            heapq.heappushpop(self.numsList, val)
        return self.numsList[0]

# KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


