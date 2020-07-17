# Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return
the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 0
        nextNumber = float('inf')
        for i in range(len(nums)):
            if nums[i] != nextNumber:
                nums[count] = nums[i]
                nextNumber = nums[i]
                count += 1
        return count



# Remove Duplicates from Sorted Array II - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return 
the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        j = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j