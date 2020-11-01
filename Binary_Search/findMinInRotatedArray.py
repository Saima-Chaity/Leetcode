# Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

'''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        return self.findMinValue(nums, left, right)

    def findMinValue(self, nums, left, right):

        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# Find Minimum in Rotated Sorted Array II - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        low = 0
        high = len(nums) - 1
        
        if nums[high] > nums[0]:
            return nums[0]

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == nums[high]: 
                if nums[mid] == nums[low]: # [10, 5, 10, 10, 10] or [10, 10, 10, 5, 10] 
                    low += 1 # or high = high-1 # min could be on either side，we just narrow the interval
                else:
                    high = mid
            elif nums[mid] > nums[high]: 
                low = mid + 1
            else:
                high = mid
        return nums[low]


