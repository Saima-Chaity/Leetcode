'''Find the number of occurrences of an element in a sorted array 
Given a sorted array of n elements, possibly with duplicates, find the number of occurrences of the target element.

Example 1:

Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
Output: 3
Example 2:

Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 6
Output: 0
Example 3:

Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 5
Output: 4
Expected O(logn) time solution.'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                while low < high and nums[low] < nums[mid]:
                    low += 1
                while low < high and nums[high] > nums[mid]:
                    high -= 1
                return high-low+1
        return high-low+1

print(Solution.searchRange((), [3, 5, 5, 5, 5, 7, 8, 8], 5))