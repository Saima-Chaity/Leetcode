# Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/
'''Given two sorted arrays nums1 and nums2 of size m and n respectively.

Return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        sortedArray = []
        i = 0
        j = 0

        while i < len(nums1) or j < len(nums2):
            if i == len(nums1) and j < len(nums2):
                sortedArray.append(nums2[j])
                j += 1
            elif i < len(nums1) and j == len(nums2):
                sortedArray.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                sortedArray.append(nums1[i])
                i += 1
            elif nums1[i] >= nums2[j]:
                sortedArray.append(nums2[j])
                j += 1

        mid = len(sortedArray) // 2
        if len(sortedArray) % 2 != 0:
            return sortedArray[mid]
        else:
            return (sortedArray[mid] + sortedArray[mid - 1]) / 2

# Time Complexity: O(m+n) where m and n is the length of nums1 and nums2 respectively
# Space Complexity: O(m+n)

# Binary Search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Take the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)
        start = 0
        end = x
        isEven = ((x + y) % 2) == 0

        while start <= end:
            partitionX = (start + end) // 2
            partitionY = ((x + y + 1) // 2) - partitionX #Adding 1 because it works well for odd and even length

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            maxRightX = float('inf') if partitionX == x else nums1[partitionX]
            maxRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= maxRightY and maxLeftY <= maxRightX:
                if isEven:
                    return (max(maxLeftX, maxLeftY) + min(maxRightX, maxRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > maxRightY:
                end = partitionX - 1
            else:
                start = partitionX + 1

# Time Complexity: O(log(min(m, n) where m and n is the length of nums1 and nums2 respectively
# Space Complexity: 1