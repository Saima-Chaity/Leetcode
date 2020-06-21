# Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/
'''There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x
        isEven = ((x + y) % 2) == 0

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = ((x + y + 1) // 2) - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            maxRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            maxRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= maxRightY and maxLeftY <= maxRightX:
                if not isEven:
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY) + min(maxRightX, maxRightY)) / 2
            elif maxLeftX > maxRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1