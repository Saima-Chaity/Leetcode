# Next Greater Element I - https://leetcode.com/problems/next-greater-element-i/
'''You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]'''

#Brute Force
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1 or not nums2:
            return []

        output = [-1] * len(nums1)

        for i in range(len(nums1)):
            isFound = False
            if nums1[i] in nums2:
                for j in range(len(nums2)):
                    if isFound and nums2[j] > nums1[i]:
                        output[i] = nums2[j]
                        break
                    if nums2[j] == nums1[i]:
                        isFound = True
        return output


#Using stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1 or not nums2:
            return []

        output = [-1] * len(nums1)
        stack = []
        mapping = {}
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > stack[-1]:
                mapping[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        while len(stack) > 0:
            mapping[stack.pop()] = -1

        for i in range(len(nums1)):
            output[i] = mapping.get(nums1[i])

        return output