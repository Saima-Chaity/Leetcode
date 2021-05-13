'''Subset Sum Problem

Given a set of non-negative integers, and a value sum, determine if there is a subset of the
given set with sum equal to given sum.

Example:

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.'''

def isSubsetSum(nums, index, sum):
    if sum == 0:
        return True
    if index == 0:
        return False
    if nums[index-1] > sum:
        return isSubsetSum(nums, index-1, sum)
    return isSubsetSum(nums, index-1, sum) or isSubsetSum(nums, index-1, sum-nums[index-1])


numsSet = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(numsSet)
if (isSubsetSum(numsSet, n, sum) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")

numsSet = [3, 34, 4, 12, 5, 2]
sum = 30
n = len(numsSet)
if (isSubsetSum(numsSet, n, sum) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")