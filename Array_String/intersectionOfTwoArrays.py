# Intersection of Two Arrays - https://leetcode.com/problems/intersection-of-two-arrays/
'''Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:'''

from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        nums2_counter = Counter(nums2)
        i = 0
        for num in nums1:
            if num in nums2_counter:
                nums2[i] = num
                del nums2_counter[num]
                i += 1
        return nums2[:i]


# 0(n) time and 0(1) space
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersections = set()
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2): 
            # skip duplicates
            while i > 0 and i < len(nums1) and nums1[i] == nums1[i-1]:
                    i += 1
            while j > 0 and j < len(nums2) and nums2[j] == nums2[j-1]:
                j += 1
                
            # still valid
            if i < len(nums1) and j < len(nums2):
                firstNumber = nums1[i]
                secondNumber = nums2[j]
                if firstNumber == secondNumber:
                    intersections.add(secondNumber)
                    i += 1
                    j += 1
                elif firstNumber > secondNumber:
                    j += 1
                else:
                    i += 1
        return intersections


# Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''Given two arrays, write a function to compute their intersection.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?'''

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        nums2_counter = Counter(nums2)
        i = 0
        for num in nums1:
            if num in nums2_counter:
                nums2_counter[num] -= 1
                nums2[i] = num
                if nums2_counter[num] == 0:
                    del nums2_counter[num]
                i += 1
        return nums2[:i]


# 0(n) time and 0(1) space
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersections = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2): 
            firstNumber = nums1[i]
            secondNumber = nums2[j]
            if firstNumber == secondNumber:
                intersections.append(secondNumber)
                i += 1
                j += 1
            elif firstNumber > secondNumber:
                j += 1
            else:
                i += 1
        return intersections
                
                