'''Maximum Number of Events That Can Be Attended
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at
any time d.

Return the maximum number of events you can attend.

Example 1:
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
'''

import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort()
        minStart = float('inf')
        maxEnd = float('-inf')
        for start, end in events:
            minStart = min(minStart, start)
            maxEnd = max(maxEnd, end)

        result = 0
        i = 0
        q = []
        for day in range(minStart, maxEnd + 1):
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(q, events[i][1])
                i += 1

            if q:
                heapq.heappop(q)
                result += 1

            while q and q[0] <= day:
                heapq.heappop(q)
        return result


'''Maximum Number of Events That Can Be Attended II
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at 
startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are 
also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. 
Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and 
the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

Example 1:
Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
'''

#Top-down approach
#for each event you can skip it OR add value of that event + value of next event which starts after this event

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        dp = [[-1] * (k + 1) for _ in range(len(events))]
        events.sort(key=lambda x: (x[0], x[1]))

        def maxEvents(current, k):
            if current >= len(events) or k == 0:
                return 0
            if dp[current][k] != -1:
                return dp[current][k]

            i = current + 1
            while i < len(events):
                if events[i][0] > events[current][1]:
                    break
                i += 1
            dp[current][k] = max(maxEvents(current + 1, k), events[current][2] + maxEvents(i, k - 1))
            return dp[current][k]

        return maxEvents(0, k)
