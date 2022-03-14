'''Element Appearing More Than 25% In Sorted Array -
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that
occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
'''

# Time - 0(logN)
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        def findIndex(target):
            left = 0
            right = len(arr) - 1
            leftMostIndex = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    right = mid - 1
                    leftMostIndex = mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            left = 0
            right = len(arr) - 1
            rightMostIndex = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    left = mid + 1
                    rightMostIndex = mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return leftMostIndex, rightMostIndex

        n = len(arr) // 4
        for i in range(0, len(arr), max(1, n)):
            left, right = findIndex(arr[i])
            if right - left + 1 > n:
                return arr[i]
