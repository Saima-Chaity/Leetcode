'''
Largest K such that both K and -K exist in array

Write a function that, given an array A of N integers, returns the largest integer K > 0
such that both values K and -K exist in array A. If there is no such integer, the function should return 0.

Example 1:

Input: [3, 2, -2, 5, -3]
Output: 3
Example 2:

Input: [1, 2, 3, -4]
Output: 0
'''

'''Sorting + Two Pointers O(nlogn)'''
def solution(nums):

    nums.sort()
    i = 0
    j = len(nums)-1
    while i < j:
        if nums[i] + nums[j] == 0:
            return nums[j]
        if abs(nums[i]) > abs(nums[j]):
            i += 1
        else:
            j -= 1
    return 0

print(solution([-5, 2, -2, 5, -3]))


''' O(n) time and space'''
def solution(nums):

    largestNum = 0
    mapping = set()
    for num in nums:
        if num * -1 in mapping:
            largestNum = max(largestNum, abs(num))
        else:
            mapping.add(num)
    return largestNum
print(solution([-41,3,2,5,41]))
