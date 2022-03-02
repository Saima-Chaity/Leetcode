# Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/
'''Given a non-empty array of integers, return the k most frequent elements.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''

# Using heap
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        mapping = Counter(nums)
        for element, freq in mapping.items():
            heapq.heappush(heap, (freq, element))
            if len(heap) > k:
                heapq.heappop(heap)
        return [element for freq, element in heap]


# Using bucket sort
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        output = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                output.append(num)
                if len(output) == k:
                    return output


# Quickselect
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.mapping = Counter(nums)  # Keys - element and values - frequency
        self.elements = list(self.mapping.keys())
        length = len(self.elements)
        self.findTopKElements(0, length - 1, length - k)
        return self.elements[length - k:]

    def findTopKElements(self, left, right, k):
        if left == right:
            return

        pivotIndex = random.randint(left, right)
        pivotIndex = self.partition(left, right, pivotIndex)

        if k == pivotIndex:
            return
        elif k < pivotIndex:
            self.findTopKElements(left, pivotIndex - 1, k)
        else:
            self.findTopKElements(pivotIndex + 1, right, k)

    def partition(self, left, right, pivotIndex):
        pivot_freq = self.mapping[self.elements[pivotIndex]]
        self.elements[right], self.elements[pivotIndex] = self.elements[pivotIndex], self.elements[right]
        low = left
        for i in range(left, right):
            if self.mapping[self.elements[i]] < pivot_freq:
                self.elements[low], self.elements[i] = self.elements[i], self.elements[low]
                low += 1
        self.elements[right], self.elements[low] = self.elements[low], self.elements[right]
        return low


