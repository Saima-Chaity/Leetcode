'''Find the Kth Smallest Sum of a Matrix With Sorted Rows
https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k.

You are allowed to choose exactly one element from each row to form an array.

Return the kth smallest array sum among all possible arrays.

Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
'''

import heapq
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        row = len(mat)
        col = len(mat[0])
        result = self.helper(mat, k)
        return result[k - 1]

    def helper(self, mat, k):
        if len(mat) == 1:
            return mat[0]
        mid = (len(mat)) // 2
        left = self.helper(mat[:mid], k)
        right = self.helper(mat[mid:], k)
        return self.merge(left, right, k)

    def merge(self, l1, l2, k):
        result = []
        if not l1 or not l2 or not k:
            return result

        heap = []
        for i in l1:
            for j in l2:
                heapq.heappush(heap, i + j)

        while heap and k:
            result.append(heapq.heappop(heap))
            k -= 1
        return result
