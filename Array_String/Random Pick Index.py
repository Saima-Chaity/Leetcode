'''Random Pick Index - https://leetcode.com/problems/random-pick-index/

Given an integer array nums with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's,
then each index should have an equal probability of returning.

Example 1:

Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]
'''


class Solution:

    def __init__(self, nums: List[int]):

        self.nums = nums

    def pick(self, target: int) -> int:
        indexes = []
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                indexes.append(i)

        return random.choice(indexes)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# 0(1) space
class Solution:

    def __init__(self, nums: List[int]):

        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        index = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                if random.randint(0, count - 1) == 0:
                    index = i
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)