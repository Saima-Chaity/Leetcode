# 132 Pattern - https://leetcode.com/problems/132-pattern/
'''Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j]
and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise return false.
Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.'''


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False

        stack = [[nums[0], nums[0]]]
        currentMin = nums[0]
        for i in range(1, len(nums)):
            current = nums[i]
            if current <= currentMin:
                currentMin = current
            else:
                while stack and current > stack[-1][0]:
                    if current < stack[-1][1]:
                        return True
                    else:
                        stack.pop()
                stack.append([currentMin, current])
        return False
