'''Partition Array into Disjoint Intervals
https://leetcode.com/problems/partition-array-into-disjoint-intervals/

Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
'''


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

        n = len(nums)
        leftMax = [0] * n
        rightMin = [0] * n

        currentMax = nums[0]
        for i in range(n):
            currentMax = max(currentMax, nums[i])
            leftMax[i] = currentMax

        currentMin = nums[-1]
        for i in range(n - 1, -1, -1):
            currentMin = min(currentMin, nums[i])
            rightMin[i] = currentMin

        for i in range(1, n):
            if leftMax[i - 1] <= rightMin[i]:
                return i


# Space - 0(1)
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

        n = len(nums)
        length = 1
        initialMax = nums[0]
        maxEncountered = 0

        for i in range(n):
            maxEncountered = max(maxEncountered, nums[i])

            if nums[i] < initialMax:
                initialMax = maxEncountered
                length = i + 1
        return length
