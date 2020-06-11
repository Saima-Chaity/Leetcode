# Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/
'''Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that
at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find the intersection point of the two runners.
        slow = nums[0]
        first = nums[0]

        while True:
            slow = nums[slow]
            first = nums[nums[first]]

            if slow == first:
                break

        # Find the "entrance" to the cycle.
        pointer1 = nums[0]
        pointer2 = slow

        while pointer1 != pointer2:
            pointer1 = nums[pointer1]
            pointer2 = nums[pointer2]
        return pointer1