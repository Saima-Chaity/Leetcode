# Move Zeroes - https://leetcode.com/problems/move-zeroes/
'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = left + 1

        while left < right and right < len(nums):
            if nums[left] != 0:
                left += 1
            elif nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1