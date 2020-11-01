# Find a local minima in an array
'''Given an array arr[0 .. n-1] of distinct integers, the task is to find a local minima in it. We say that an 
element arr[x] is a local minimum if it is less than or equal to both its neighbors.

For corner elements, we need to consider only one neighbor for comparison.
There can be more than one local minima in an array, we need to find any one of them.
Examples:

Input: arr[] = {9, 6, 3, 14, 5, 7, 4};
Output: Index of local minima is 2
The output prints index of 3 because it is 
smaller than both of its neighbors. 
Note that indexes of elements 5 and 4 are 
also valid outputs.'''

class Solution:
    def findMinimumElement(self, nums: List[int]) -> int:
        return self.findMinimum(nums, 0, len(nums)-1, len(nums))
    
    def findMinimum(self, nums, low, high, numsLength):
        mid = low + (high-low) // 2
        if (mid == 0 or nums[mid] < nums[mid-1]) and (mid == numsLength-1 or nums[mid] < nums[mid+1]):
            return mid
        elif mid > 0 and nums[mid] > nums[mid-1]: #search in the left side
            return self.findMinimum(nums, low, mid-1, numsLength)
        else:
            return self.findMinimum(nums, mid+1, high, numsLength) #search in the right side
