'''Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

You are given an integer array nums and you have to return a new counts array. The counts array has the property
where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        count = [0] * len(nums)
        arr = [[value, index] for index, value in enumerate(nums)]

        def merge(arr, left, right, mid):
            i = left
            j = mid + 1
            temp = []
            while i <= mid and j <= right:
                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    j += 1
                else:
                    count[arr[i][1]] += j - (mid + 1)
                    temp.append(arr[i])
                    i += 1

            while i <= mid:
                count[arr[i][1]] += right - mid
                temp.append(arr[i])
                i += 1

            while j <= right:
                temp.append(arr[j])
                j += 1

            for i in range(left, right + 1):
                arr[i] = temp[i - left]

        def merge_sort(arr, left, right):
            if left < right:
                mid = left + (right - left) // 2
                merge_sort(arr, left, mid)
                merge_sort(arr, mid + 1, right)
                merge(arr, left, right, mid)

        merge_sort(arr, 0, len(arr) - 1)
        return count
