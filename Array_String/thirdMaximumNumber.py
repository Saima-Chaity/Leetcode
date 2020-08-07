# Third Maximum Number - https://leetcode.com/problems/third-maximum-number/
'''Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.'''

import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        heap = [-1 * num for num in nums]
        heapq.heapify(heap)

        if len(heap) < 3:
            return -heap[0]  # Maximum number

        heapq.heappop(heap)
        heapq.heappop(heap)
        return -heap[0]
