# Find Peak Element - https://leetcode.com/problems/find-peak-element/
'''A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.
Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.'''

#Linear Scan
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        i = 0
        while i < len(nums)-1:
            if nums[i] <= nums[i+1]:
                i += 1
                continue
            else:
                return i
        return i if i == len(nums)-1 else -1


#Iterative Binary Search
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        low = 0
        high = len(nums)-1
        while low < high:
            mid = low + (high-low) // 2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid + 1
        return low
                
        