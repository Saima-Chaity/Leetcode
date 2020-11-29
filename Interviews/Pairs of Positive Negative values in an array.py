'''Pairs of Positive Negative values in an array
Given an array of distinct integers, print all the pairs having positive value and negative value of a
number that exists in the array. We need to print pairs in order of their occurrences.
A pair whose any element appears first should be printed first.

Examples:

Input  :  arr[] = { 1, -3, 2, 3, 6, -1 }
Output : -1 1 -3 3

Input  :  arr[] = { 4, 8, 9, -4, 1, -1, -8, -9 }
Output : -1 1 -4 4 -8 8 -9 9'''

def printPairs(nums):
    nums.sort()
    negativeIndex = 0
    positiveIndex = len(nums) - 1

    while negativeIndex < len(nums):
        if nums[negativeIndex] < 0:
            negativeIndex += 1
        else:
            break

    while positiveIndex > 0:
        if nums[positiveIndex] > 0:
            positiveIndex -= 1
        else:
            break

    negativeIndex = negativeIndex - 1
    positiveIndex = positiveIndex + 1

    while negativeIndex >= 0 and positiveIndex < len(nums):
        if abs(nums[negativeIndex]) == nums[positiveIndex]:
            print(nums[negativeIndex], nums[positiveIndex], end=" ")
            negativeIndex -= 1
            positiveIndex += 1
        elif abs(nums[negativeIndex]) < nums[positiveIndex]:
            negativeIndex -= 1
        elif abs(nums[negativeIndex]) > nums[positiveIndex]:
            positiveIndex += 1


printPairs([1, -3, 2, 3, 6, -1])
print("\n")
printPairs([4, 8, 9, -4, 1, -1, -8, -9])