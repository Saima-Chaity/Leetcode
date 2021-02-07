# Minimum Difficulty of a Job Schedule - https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
'''You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job,
you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of
difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a
job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is
jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule
for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
'''


'''
dfs help find the the minimum difficulty
if start work at ith job with d days left.

If d = 1, only one day left, we have to do all jobs,
return the maximum difficulty of jobs.

Time complexity O(nnd)
Space complexity O(nd)'''

# Top down with memoizarion
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        def getMinDifficulty(index, jobDifficulty, d):

            if d <= 0:
                return float('inf')

            if d == 1:
                if index < len(jobDifficulty):
                    return max(jobDifficulty[index:])
                return float('inf')

            if (d, index) in self.memo:
                return self.memo[(d, index)]

            minimumDifficulty = float('inf')
            for i in range(index, len(jobDifficulty)):
                minimumDifficulty = min(minimumDifficulty,
                                        getMinDifficulty(i + 1, jobDifficulty, d - 1) + max(jobDifficulty[index:i + 1]))

            self.memo[(d, index)] = minimumDifficulty
            return minimumDifficulty

        self.memo = {}
        return getMinDifficulty(0, jobDifficulty, d) if len(jobDifficulty) >= d else -1


'''Solution 4 with the stack is brilliant. I spend a lot of time understanding it.
Here is my understanding:
The reason why the stack can speed up is that we don't have to check every possible cut off 
(the value of j in solution 2/3).
The stack keeps the index of monotonically decreasing number in A. When checking A[i], assuming that the last 
number that larger than A[i] is A[t] (stack[-1]=t after poping), there are two possible situations:

For possible cut off index m in A[t: i]: t<=m <i:
We need to check possible cut off. And the corresponding code is in the while loop: " j = stack.pop() 
dp2[i] = min(dp2[i], dp2[j] - A[j] + A[i])"
Here we only check those items pop from the stack (they have a smaller index but larger value). we can 
see that the items pop before this loop were smaller, they were dominant by the items left in the stack. 
So we don't have to check those items.
For possile cut off index m in A[:t]: m <t
since A[t] is the last number that larger than A[i], we know A[t] = max(A[t:i]), for any index m 
before t(m<t), we have max(A[m:i]) = max(A[m:t]) : we can directly "dp2[i] = min(dp2[i], dp2[stack[-1]])"
Remeber that in 2D Array: dp[d][i] means the min difficulty in d days for i jobs, it equals 
dp[d][i] = dp[d][t] (t < i so dp[d][t] should have already been caculated)'''

'''Time O(nd)
Space O(n)
'''
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        A = jobDifficulty
        n = len(A)
        if n < d: return -1
        dp, dp2 = [float('inf')] * n, [0] * n
        for d in range(d):
            stack = []
            for i in range(d, n):
                dp2[i] = dp[i - 1] + A[i] if i else A[i]
                while stack and A[stack[-1]] <= A[i]:
                    j = stack.pop()
                    dp2[i] = min(dp2[i], dp2[j] - A[j] + A[i])
                if stack:
                    dp2[i] = min(dp2[i], dp2[stack[-1]])
                stack.append(i)
            dp, dp2 = dp2, dp
        return dp[-1]