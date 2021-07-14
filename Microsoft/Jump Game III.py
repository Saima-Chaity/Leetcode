'''Jump Game III - https://leetcode.com/problems/jump-game-iii/

Given an array of non-negative integers arr, you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3
'''

'''Time and Space - 0(N)'''
'''BFS'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        q = [start]
        while q:
            index = q.pop(0)
            if arr[index] == 0:
                return True
            if arr[index] < 0:
                continue
            for i in [index + arr[index], index - arr[index]]:
                if 0 <= i < len(arr):
                    q.append(i)
            arr[index] = -arr[index]
        return False


'''DFS'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            arr[start] = -arr[start]
            return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        return False
