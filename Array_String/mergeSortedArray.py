# Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/
'''Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        pointer1 = m - 1
        pointer2 = n - 1
        lastIndex = m + n - 1

        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[lastIndex] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[lastIndex] = nums2[pointer2]
                pointer2 -= 1
            lastIndex -= 1
        while pointer1 < 0 and pointer2 >= 0:
            nums1[pointer2] = nums2[pointer2]
            pointer2 -= 1


