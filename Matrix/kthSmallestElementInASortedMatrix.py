'''Kth Smallest Element in a Sorted Matrix -
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the
kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.'''

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap, matrix[i][j])

        for i in range(k):
            k_smallest = heapq.heappop(heap)
        return k_smallest

# Quick Select
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        self.findKthSmallest(0, row * col - 1, k - 1, matrix)
        x, y = (k - 1) // col, (k - 1) % col
        return matrix[x][y]

    def findKthSmallest(self, left, right, k, matrix):
        if left > right:
            return

        pivotIndex = random.randint(left, right)
        pivotIndex = self.partition(matrix, left, right, pivotIndex)

        if k == pivotIndex:
            return
        elif k < pivotIndex:
            self.findKthSmallest(left, pivotIndex - 1, k, matrix)
        else:
            self.findKthSmallest(pivotIndex + 1, right, k, matrix)

    def partition(self, matrix, left, right, pivotIndex):
        col = len(matrix[0])
        pivot = matrix[pivotIndex // col][pivotIndex % col]
        self.swap(right, pivotIndex, matrix)

        low = left
        for i in range(left, right):
            if matrix[i // col][i % col] < pivot:
                self.swap(low, i, matrix)
                low += 1
        self.swap(right, low, matrix)
        return low

    def swap(self, x, y, matrix):
        col = len(matrix[0])
        matrix[x // col][x % col], matrix[y // col][y % col] = matrix[y // col][y % col], matrix[x // col][x % col]
        return matrix
