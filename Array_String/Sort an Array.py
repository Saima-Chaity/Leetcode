# Sort an Array - https://leetcode.com/problems/sort-an-array/
'''Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeArr(leftArr, rightArr):
            result = []
            i = 0
            j = 0
            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] <= rightArr[j]:
                    result.append(leftArr[i])
                    i += 1
                else:
                    result.append(rightArr[j])
                    j += 1

            while i < len(leftArr):
                result.append(leftArr[i])
                i += 1

            while j < len(rightArr):
                result.append(rightArr[j])
                j += 1

            return result

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        leftList = self.sortArray(nums[:mid])
        rightList = self.sortArray(nums[mid:])
        return mergeArr(leftList, rightList)
