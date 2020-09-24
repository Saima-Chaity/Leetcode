# Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/
'''Find the kth largest element in an unsorted array. Note that it is the kth largest element in
the sorted order, not the kth distinct element.

Input: [3,2,1,5,6,4] and k = 2
Output: 5'''

# Using heap
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# Quick sort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthSmallest(0, len(nums) - 1, len(nums) - k, nums)

    def findKthSmallest(self, left, right, k, nums):
        if left == right:
            return nums[left]

        pivotIndex = random.randint(left, right)
        pivotIndex = self.partition(nums, left, right, pivotIndex)

        if k == pivotIndex:
            return nums[k]
        elif k < pivotIndex:
            return self.findKthSmallest(left, pivotIndex - 1, k, nums)
        else:
            return self.findKthSmallest(pivotIndex + 1, right, k, nums)

    def partition(self, nums, left, right, pivotIndex):
        pivot = nums[pivotIndex]
        nums[right], nums[pivotIndex] = nums[pivotIndex], nums[right]
        low = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
        nums[right], nums[low] = nums[low], nums[right]
        return low

