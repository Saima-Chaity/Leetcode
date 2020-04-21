'''Given a list of positive integers nums and an int target, return indices of the two numbers such that
they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.'''

class Solution:
    def findPair(nums, target):
        expectedSum = target - 30
        map = {}
        maxNum = -1
        output = [-1, -1]
        for index, num in enumerate(nums):
            secondNum = expectedSum - num
            if secondNum not in map:
                map[num] = index
            else:
                if num > maxNum or secondNum > maxNum:
                    output[0] = map[secondNum]
                    output[1] = index
                    maxNum = max(secondNum, num)
        return output if output != [-1, -1] else []

print(Solution.findPair([1, 10, 25, 35, 60], 90))