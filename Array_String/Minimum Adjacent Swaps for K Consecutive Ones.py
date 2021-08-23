'''Minimum Adjacent Swaps for K Consecutive Ones
https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move,
you can choose two adjacent indices and swap their values.

Return the minimum number of moves required so that nums has k consecutive 1's.

Example 1:

Input: nums = [1,0,0,1,0,1], k = 2
Output: 1
Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.
Example 2:

Input: nums = [1,0,0,0,0,0,1,1], k = 3
Output: 5
Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].
Example 3:

Input: nums = [1,1,0,1], k = 2
Output: 0
Explanation: nums already has 2 consecutive 1's.'''


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:

        position = [index for index, num in enumerate(nums) if num]
        n = len(position)
        prefix_sum_of_ones = {-1: 0}
        for i in range(n):
            prefix_sum_of_ones[i] = prefix_sum_of_ones[i - 1] + position[i]

        answer = float('inf')
        for i in range(n - k + 1):
            mid = i + k // 2
            right = prefix_sum_of_ones[i + k - 1] - prefix_sum_of_ones[mid]
            left = prefix_sum_of_ones[mid - 1] - prefix_sum_of_ones[i - 1]
            answer = min(answer, right - left + (position[mid] if k % 2 == 0 else 0))

        radius = (k - 1) // 2
        answer -= radius * (radius + 1) // 2 * 2 + ((radius + 1) if k % 2 == 0 else 0)
        return answer