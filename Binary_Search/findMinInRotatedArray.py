# Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

'''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.'''


class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1
        if nums[high] > nums[low]:
            return nums[low]

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1


#Another Approach
class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1

        if nums[high] > nums[low]:
            return nums[low]

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]

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

        if nums[high] > nums[low]:
            return nums[low]

        while low < high:
            mid = low + (high - low) // 2
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]

