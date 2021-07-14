# Jump Game - https://leetcode.com/problems/jump-game/
'''Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lastPosition = len(nums)-1       
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= lastPosition:
                lastPosition = i
        return lastPosition == 0


# Another approach
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i <= farthest:
                farthest = max(farthest, i + nums[i])
        return farthest >= len(nums)-1


# Jump Game II - https://leetcode.com/problems/jump-game-ii/
'''Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, 
then 3 steps to the last index.'''

class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        farthest = 0
        current_jump_end = 0
        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end and i != len(nums) - 1:
                jumps += 1
                current_jump_end = farthest
        return jumps