# Sort Colors - https://leetcode.com/problems/sort-colors/
'''Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) - 1
        zero = 0
        while left <= right:
            if nums[left] == 0:
                nums[left], nums[zero] = nums[zero], nums[left]
                left += 1
                zero += 1
            elif nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1

# Another approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0:c0 + c1] = [1] * c1
        nums[c0 + c1:] = [2] * c2
