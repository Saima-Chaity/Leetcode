'''
Count Inversions in an array
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array
is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count
is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
Example:

Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).


Input: arr[] = {3, 1, 2}
Output: 2

Explanation: Given array has two inversions:
(3, 1), (3, 2)
'''

'''Time Complexity: O(n log n), The algorithm used is divide and conquer, So in each level one full 
array traversal is needed and there are log n levels so the time complexity is O(n log n).
Space Complexity: O(n), Temporary array.'''

class Solution:
    def countInversion(self, nums):

        def mergeArr(leftArr, rightArr):
            inversionCount = 0
            i = 0
            j = 0
            result = []
            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] <= rightArr[j]:
                    result.append(leftArr[i])
                    i += 1
                else:
                    result.append(rightArr[j])
                    inversionCount += len(leftArr) - i
                    j += 1

            while i < len(leftArr):
                result.append(leftArr[i])
                i += 1

            while j < len(rightArr):
                result.append(rightArr[j])
                j += 1

            return result, inversionCount


        def sortAnArray(nums):
            nonlocal inversionCount
            if len(nums) <= 1:
                return nums, 0
            mid = len(nums) // 2
            leftArr, leftInversion = sortAnArray(nums[:mid])
            rightArr, rightInversion = sortAnArray(nums[mid:])
            inversionCount = leftInversion + rightInversion
            mergedArr, count = mergeArr(leftArr, rightArr)
            inversionCount += count
            return mergedArr, inversionCount

        inversionCount= 0
        sortAnArray(nums)
        return inversionCount



nums = [8, 4, 2, 1]
print(Solution.countInversion((), nums)) # 6

nums = [3, 1, 2]
print(Solution.countInversion((), nums)) # 2

nums = [1, 9, 6, 4, 5]
print(Solution.countInversion((), nums)) # 5

nums = [5, 2, 6, 1]
print(Solution.countInversion((), nums)) # 4

nums = [1, 9, 7, 8, 5]
print(Solution.countInversion((), nums)) # 5

nums = [6, 3, 7, 1, 5, 8, 2, 4]
print(Solution.countInversion((), nums)) # 15

nums = [-1, -1]
print(Solution.countInversion((), nums)) # 0

nums = [5, 4, 1, 2,]
print(Solution.countInversion((), nums)) # 5
