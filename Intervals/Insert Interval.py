# Insert Interval - https://leetcode.com/problems/insert-interval/
'''Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        output = []
        startTime = float('inf')
        endTime = float('-inf')
        foundOverlap = False
        for index, interval in enumerate(intervals):
            low = max(interval[0], newInterval[0])
            high = min(interval[1], newInterval[1])
            if low <= high:
                startTime = min(startTime, min(interval[0], newInterval[0]))
                endTime = max(endTime, max(interval[1], newInterval[1]))
                foundOverlap = True
            else:
                output.append(interval)

        if foundOverlap:
            output.append([startTime, endTime])
        else:
            output.append(newInterval)
        output.sort(key=lambda x: x[0])
        return output