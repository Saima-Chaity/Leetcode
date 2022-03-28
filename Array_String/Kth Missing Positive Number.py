'''Kth Missing Positive Number - https://leetcode.com/problems/kth-missing-positive-number/

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Find the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
'''


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        if k <= arr[0] - 1:
            return k
        k -= arr[0] -1
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1] - 1
            if diff >= k:
                return arr[i-1] + k
            k -= diff
        return arr[len(arr)-1] + k


# Binary Search
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k # left == right + 1, so arr[right] + k - (arr[right] - right - 1) == k + right + 1 == k + left