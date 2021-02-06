'''Given an array of driver's ratings over N days.
Value over a period = (Contiuous sum * Minimum rating in that period)

eg: [3, 1, 6, 4, 5, 2]
Value could be (3+1+6+4+5+2) * 1 = 21.

Find the maximum value.
Here max value is (6+4+5) * 4 = 60.'''

'''O(n) time'''
class Solution:
    def driversRatings(self, ratings):

        prefixSum = [0] * (len(ratings) + 1)
        for i in range(0, len(ratings)):
            prefixSum[i+1] = prefixSum[i] + ratings[i]

        stack = []
        leftIndex = [-1] * len(ratings)
        for i in range(len(ratings)):
            while stack and ratings[stack[-1]] > ratings[i]:
                stack.pop()
            leftIndex[i] = -1 if not stack else stack[-1]
            stack.append(i)

        stack = []
        rightIndex = [len(ratings)] * len(ratings)
        for i in range(len(ratings)-1, -1, -1):
            while stack and ratings[stack[-1]] > ratings[i]:
                stack.pop()
            rightIndex[i] = len(ratings) if not stack else stack[-1]
            stack.append(i)

        maximum = float('-inf')
        for i in range(len(ratings)):
            current = ratings[i] * (prefixSum[rightIndex[i]] - prefixSum[leftIndex[i]+1])
            maximum = max(maximum, current)
        return maximum


ratings = [3, 1, 6, 4, 5, 2]
print(Solution.driversRatings((), ratings)) # 60