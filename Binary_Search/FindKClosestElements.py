# Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/
'''Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. 
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]'''

'''Complexity
Time O(log(N - K)) to binary research and find result
Space O(K) to create the returned list.'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if arr[0] > x:
            return arr[:k]
        if arr[-1] < x:
            return arr[-k:]

        left = 0
        right = len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == arr[mid + k]:
                if x > arr[mid]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if abs(x - arr[mid]) > abs(arr[mid + k] - x):
                    left = mid + 1
                else:
                    right = mid
        return arr[left:left + k]

# Reference -
# https://leetcode.com/problems/find-k-closest-elements/discuss/462664/Python-binary-search-with-detailed-explanation