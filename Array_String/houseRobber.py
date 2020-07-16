# House Robber - https://leetcode.com/problems/house-robber/
'''You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent
houses have security system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine
the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.'''

class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

# House Robber II - https://leetcode.com/problems/house-robber-ii/
'''You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed. All houses at this place are arranged in a circle. That means the first
house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine
the maximum amount of money you can rob tonight without alerting the police.

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.'''

# Two pointer
class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev = 0
        current = 0
        for i in range(len(nums) - 1): # Rob from 1st house to n-1
            prev, current = current, max(prev + nums[i], current)
        n1 = current

        prev = 0
        current = 0
        for i in range(1, len(nums)): # Rob from 2nd house to n
            prev, current = current, max(prev + nums[i], current)
        n2 = current

        return max(n1, n2)

# Dynamic programming
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def house_robber(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[-1]

        if len(nums) <= 2:
            return max([0] + nums)
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))

# House Robber III - https://leetcode.com/problems/house-robber-iii/
'''The thief has found himself a new place for his thievery again. There is only one entrance to 
this area, called the "root." Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.cache = {}
        return self.robHouse(root)

    def robHouse(self, root):
        if not root:
            return 0
        if root in self.cache:
            return self.cache[root]

        robValue = root.val + self.robChildren(root.left) + self.robChildren(root.right)
        noRobValue = self.robHouse(root.left) + self.robHouse(root.right)
        profit = max(robValue, noRobValue)
        self.cache[root] = profit
        return profit

    def robChildren(self, root):
        if not root:
            return 0
        left = 0
        right = 0
        if root.left:
            left = self.robHouse(root.left)
        if root.right:
            right = self.robHouse(root.right)
        return left + right