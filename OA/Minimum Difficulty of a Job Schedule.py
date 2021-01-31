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