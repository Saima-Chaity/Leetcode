'''Find The Maximum Available Disk Space

A Company performing an analysis on the computers at one of its offices. The computers are
spaced along a single row.

The analysis is performed in the following way:

Choose a contiguous segment of a certain number of computers, starting from the beginning of the row.
Analyze the available hard disk space on each of the computers. Determine the minimum available
disk space within this segment.
After performing these steps for the first segment, it is then repeated for the next segment,
continuing this procedure until the end of the row (i.e. if the segment size is 4, computers 1
to 4 would be analyzed, then 2 to 5, etc.)
Given this analysis procedure, write an algorithm to find the maximum available disk space
among all the minima that are found during the analysis.

Input
The input consists of three arguments:

numComputer: an integer representing the number of computers

hardDiskSpace: a list of integers representing the hard disk space of the computers

segmentLength: an integer representing the length of the contiguous segment of computers to be
considered in each iteration

Output
Return an integer representing the maximum available disk space among all the minima that are
found during the analysis.

Constraints
1 ≤ numComputer ≤ 10^6

1 ≤ segmentLength ≤ numComputer

1 ≤ hardDiskSpace[i] ≤ 10^9

0 ≤ i < numComputer

Examples
Example 1:
Input:
numComputer = 3

hardDiskSpace = [8,2,4]

segmentLength = 2

Output: 2
Explanation:
In this array of computers, the subarrays of size 2 are [8,2] and [2,4]. Thus, the initial analysis
returns 2 and 2 because those are the minima for the segments. Finally, the maximum of these values
is 2. Therefore, the answer is 2.

Hint:
Time Complexity = O(n)

Extra Space Complexity = O(n)
'''

from collections import deque
class Solution:
    def maxDiskSpace(self, numComputer, hardDiskSpace, segmentLength):
        def cleanQueue(index):
            if q and q[0] == index - k:
                q.popleft()

            while q and hardDiskSpace[index] < hardDiskSpace[q[-1]]:
                q.pop()

        output = []
        q = deque()
        k = segmentLength
        for i in range(k):
            cleanQueue(i)
            q.append(i)
        output.append(hardDiskSpace[q[0]])

        for i in range(k, len(hardDiskSpace)):
            cleanQueue(i)
            q.append(i)
            output.append(hardDiskSpace[q[0]])
        print(output)
        return max(output)

numComputer = 3
hardDiskSpace = [8, 2, 4]
segmentLength = 2
print(Solution.maxDiskSpace((), numComputer, hardDiskSpace, segmentLength)) #Output: 2

numComputer = 5
hardDiskSpace = [8, 3, 4, 5, 4]
segmentLength = 2
print(Solution.maxDiskSpace((), numComputer, hardDiskSpace, segmentLength)) #Output: 2