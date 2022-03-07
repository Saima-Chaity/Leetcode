'''Monotonic Array - https://leetcode.com/problems/monotonic-array/

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing
if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:

Input: nums = [1,2,2,3]
Output: true
'''


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        increasing = False
        decreasing = False
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                increasing = True
            elif nums[i - 1] > nums[i]:
                decreasing = True
            if increasing and decreasing:
                return False
        return True

# Return count
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        increasing = False
        decreasing = False
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                if decreasing:
                    count += 1
                    decreasing = False
                increasing = True
            elif nums[i] > nums[i + 1]:
                decreasing = True
                if increasing:
                    increasing = False
                    count += 1
        return count