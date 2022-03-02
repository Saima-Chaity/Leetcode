'''Check If a Number Is Majority Element in a Sorted Array
https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

Given an integer array nums sorted in non-decreasing order and an integer target, return true if
target is a majority element, or false otherwise.

A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

Example 1:

Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.
'''


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2
        if nums[mid] == target:
            while left < right and nums[left] < nums[mid]:
                left += 1
            while left < right and nums[right] > nums[mid]:
                right -= 1
            if right - left + 1 > n // 2:
                return True
        return False

