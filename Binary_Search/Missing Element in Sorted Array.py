'''Missing Element in Sorted Array - https://leetcode.com/problems/missing-element-in-sorted-array/

Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an
integer k, return the kth missing number starting from the leftmost number of the array.

Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.
Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
'''


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1] - 1
            if diff >= k:
                return nums[i - 1] + k
            k -= diff
        return nums[len(nums) - 1] + k

# Binary Search
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        def getMissingCount(index):
            # all missing count from 0 to the current index
            return nums[index] - nums[0] - index

        n = len(nums) - 1
        if k > getMissingCount(n):
            return nums[-1] + k - getMissingCount(n)

        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if getMissingCount(mid) < k:
                left = mid + 1
            else:
                right = mid
        return nums[left - 1] + k - getMissingCount(left - 1)  # result lies between left-1 to left
                                                               # remove all the missing count before left - 1
