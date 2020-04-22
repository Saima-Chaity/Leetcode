# Intersection of Three Sorted Arrays - https://leetcode.com/problems/intersection-of-three-sorted-arrays/

'''Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.'''


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        mapping = dict()
        for num in arr1:
            mapping[num] = mapping.get(num, 0) + 1

        for key, value in mapping.items():
            if key not in arr2 or key not in arr3:
                mapping[key] = ""
        return sorted(key for key, value in mapping.items() if value != '')