# The K Weakest Rows in a Matrix - https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
'''Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of
the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j,
or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row,
that is, always ones may appear first and then zeros.

Example 1:

Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]'''

import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        row = len(mat)
        col = len(mat[0])
        strengths = []

        def getCount(row):
            low = 0
            high = col

            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low

        for index, row in enumerate(mat):
            strength = getCount(row)
            entry = (-strength, -index)
            if len(strengths) < k or entry > strengths[0]:
                heapq.heappush(strengths, entry)
            if len(strengths) > k:
                heapq.heappop(strengths)

        indexes = []
        while strengths:
            strength, i = heapq.heappop(strengths)
            indexes.append(-i)
        return indexes[::-1]


