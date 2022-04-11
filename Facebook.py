'''Unique Paths Variant
You are given a method signature of List<String> uniquePaths(int n), where n is the size of an n x n 2-dimensional
array. You have to return a dynamic array of all possible paths, where you may only go down and right--a single move
right will be represented by the character R, and a single move down will be represented by the character D. Each
string represents each possible path from the top-most index to the bottom-most index. Backtracking may be used to
achieve this.
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def backTrack(i, j, path):
            if i == m - 1 and j == n - 1:
                result.append(path)
                return
            if i == m or j == n:
                return
            backTrack(i + 1, j, path + ['D'])
            backTrack(i, j + 1, path + ['R'])

        backTrack(0, 0, [])
        return result

'''Given N sorted arrays, return a merged sorted array removing any duplicate values. 
For example [1,4,5,5,6], [2,3,4,5], [1,2,7,8] return [1,2,3,4,5,6,7,8].'''

class Solution:
    def mergeKLists(self, lists):

        if not lists:
            return None

        def merge(l1, l2):
            result = [0] * (len(l1)+len(l2))
            i = 0
            j = 0
            index = 0
            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    result[index] = l1[i]
                    i += 1
                else:
                    result[index] = l2[j]
                    j += 1
                index += 1

            while i < len(l1):
                result[index] = l1[i]
                i += 1
                index += 1

            while j < len(l2):
                result[index] = l2[j]
                j += 1
                index += 1
            return result

        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])
            interval *= 2

        result = lists[0] if len(lists) > 0 else lists
        j = 1
        for i in range(1, len(result)):
            if result[i] != result[i-1]:
                result[j] = result[i]
                j += 1
        return result[:j]

sol = Solution()
print(sol.mergeKLists([[1,4,5,5,6],[2,3,4,5],[1,2,7,8]]))  #[1,2,3,4,5,6,7,8]


'''Given two arrays of integers a and b of the same length, find the number of pairs (i, j) such that i <=j
and a[i] - b[j] = a[j] - b[i].

Example:

. For a= [2, -2, 5, 3] and b= [1, 5, -1, 1], the output should be solution (a, b) = 6.

. For (1,5) = (0, 0) equality holds: a [0] b[0] = 2 = 1 = 1 and a[0] - b[0] =2-1=1

. For (1, 3) = (0, 1) equality holds: a [0] b[1]= 2 - 5 = -3 and - b[0]= (-2) - 1 = -3,

. For (1, 3) = (0, 2) equality doesn't hold: a[0] - b[2] 2 - (-1) = 3 and a [2] b[0] = 5-1-4.
'''

class Solution:
    def getPairs(self, num1, num2):

        mapping = {}
        for a, b in zip(num1, num2):
            mapping[(a+b)] = mapping.get((a+b), 0) + 1

        result = 0
        for key, value in mapping.items():
            result += (value * (value-1))//2
        return result + len(num1)

pairs = Solution()
print(pairs.getPairs([2, -2, 5, 3], [1, 5, -1, 1]))
