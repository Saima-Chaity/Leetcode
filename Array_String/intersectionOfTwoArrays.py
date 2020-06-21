# Intersection of Two Arrays - https://leetcode.com/problems/intersection-of-two-arrays/
'''Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:'''


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapping = dict()
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        for num in nums1:
            mapping[num] = 1

        output = set()
        for num in nums2:
            if mapping:
                if num in mapping:
                    output.add(num)
                    del mapping[num]
            else:
                break
        return output