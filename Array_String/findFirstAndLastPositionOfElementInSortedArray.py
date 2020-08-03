'''Find First and Last Position of Element in Sorted Array -
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(nums, target, isLeft):

            low = 0
            high = len(nums)
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] > target or (isLeft and nums[mid] == target):
                    high = mid
                else:
                    low = mid + 1
            return low

        leftIndex = search(nums, target, True)
        if leftIndex == len(nums) or nums[leftIndex] != target:
            return [-1, -1]
        rightIndex = search(nums, target, False)
        return [leftIndex, rightIndex - 1]

# Another approach
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                while left < right and nums[left] < nums[mid]:
                    left += 1
                while left < right and nums[right] > nums[mid]:
                    right -= 1
                return [left, right]
        return [-1, -1]


