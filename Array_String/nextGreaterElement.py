# Next Greater Element I - https://leetcode.com/problems/next-greater-element-i/
'''You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]'''

from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapping = defaultdict(list)
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i] and nums2[i] not in mapping:
                    mapping[nums2[i]] = nums2[j]
                    break

        for i in range(len(nums1)):
            if nums1[i] in mapping:
                nums1[i] = mapping[nums1[i]]
            else:
                nums1[i] = -1
        return nums1


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


# Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/
'''Given a circular array (the next element of the last element is the first element of the array), print the Next 
Greater Number for every element. The Next Greater Number of a number x is the first greater number to its 
traversing-order next in the array, which means you could search circularly to find its next greater number. 
If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        stack = []
        result = [-1] * len(nums)

        for i in range(2 * len(nums), -1, -1):
            while stack and nums[stack[-1]] <= nums[(i) % len(nums)]:
                stack.pop()
            result[(i) % len(nums)] = nums[stack[-1]] if stack else -1
            stack.append((i) % len(nums))

        return result


# Another approach
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(0, n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                result[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return result


# Brute Force
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [-1] * n
        copyArray = nums
        for i in range(n):
            copyArray.append(nums[i])

        for i in range(n):
            for j in range(i + 1, len(copyArray)):
                if copyArray[j] > nums[i]:
                    result[i] = copyArray[j]
                    break
        return result


'''Next Greater Element III - https://leetcode.com/problems/next-greater-element-iii/
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n 
and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 
32-bit integer, return -1.

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:

        if n >= 2 ** 31 - 1:
            return -1

        nums = list(str(n))

        def reverse(nums, start):
            i = start
            j = len(nums) - 1

            while i < j:
                swap(nums, i, j)
                i += 1
                j -= 1

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:  # Find first decreasing number
            i -= 1

        if i < 0:
            return -1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:  # Find increasing number greater than number at i
                j -= 1
            swap(nums, i, j)
        reverse(nums, i + 1)

        result = int("".join(nums))
        return -1 if result > 2 ** 31 - 1 or result < n else result