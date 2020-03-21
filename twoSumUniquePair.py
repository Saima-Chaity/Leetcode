'''Given an int array nums and an int target, find how many unique pairs in the array such that their sum is
equal to target. Return the number of pairs.'''
# Input: nums = [1, 1, 2, 45, 46, 46], target = 47
# Output: 2
# Explanation:
# 1 + 46 = 47
# 2 + 45 = 47

########################
# Input: nums = [1, 5, 1, 5], target = 6
# Output: 1
# Explanation:
# [1, 5] and [5, 1] are considered the same.

class Solution:
    def uniquePair(nums, target):
        pairs = set()
        result = set()

        for num in nums:
            secondNum = target - num
            if secondNum in pairs:
                output = (num, secondNum) if num > secondNum else (secondNum, num)
                result.add(output)
            pairs.add(num)
        return len(result)

print(Solution.uniquePair([1, 1], 2))