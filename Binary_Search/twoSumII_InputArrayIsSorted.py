# Two Sum II - Input array is sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''Given an array of integers that is already sorted in ascending order, find two numbers such that
they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        mapping = {}

        for index, num in enumerate(numbers):
            secondNum = target - num
            if secondNum not in mapping:
                mapping[num] = index + 1
            else:
                return [mapping[secondNum], index + 1]


# Binary Search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            mid = left + (right - left) // 2
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total < target:
                if numbers[mid] + numbers[right] < target:
                    left = mid
                else:
                    left += 1
            else:
                if numbers[mid] + numbers[left] > target:
                    right = mid
                else:
                    right -= 1
        return [-1, -1]


# Another approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def findRemaining(start, target):
            left = start
            right = len(numbers) - 1
            while left < right:
                mid = left + (right - left) // 2
                if numbers[mid] == target:
                    return mid
                if numbers[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left if numbers[left] == target else False

        for i in range(len(numbers)):
            remaining = target - numbers[i]
            index = findRemaining(i + 1, remaining)
            if index:
                return [i + 1, index + 1]
