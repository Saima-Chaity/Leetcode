# Meeting Rooms - https://leetcode.com/problems/meeting-rooms/
'''Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.'''
# Input: [[0,30],[5,10],[15,20]]
# Output: false
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda x: x[0])

        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] > intervals[i + 1][0]:
                return False
            i += 1
        return True


# Meeting Rooms II - https://leetcode.com/problems/meeting-rooms-ii/
'''Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.'''

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

#Priority Queues
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        free_rooms = []

        intervals.sort(key=lambda x: x[0])

        heapq.heappush(free_rooms, intervals[0][1])

        for interval in intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, interval[1])
        return len(free_rooms)

#Chronological Ordering
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        startPointer = 0
        endPointer = 0
        usedRooms = 0

        startTime = sorted([i[0] for i in intervals])
        endTime = sorted([i[1] for i in intervals])

        while startPointer < len(intervals):
            if startTime[startPointer] >= endTime[endPointer]:
                usedRooms -= 1
                endPointer += 1
            usedRooms += 1
            startPointer += 1
        return usedRooms


# Merge Intervals - https://leetcode.com/problems/merge-intervals/
'''Given a collection of intervals, merge all overlapping intervals.'''
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        stack = [intervals[0]]
        i = 1

        while i < len(intervals):
            if stack[-1][1] >= intervals[i][0]:
                stack[-1] = [min(stack[-1][0], intervals[i][0]), max(stack[-1][1], intervals[i][1])]
            else:
                stack.append(intervals[i])
            i += 1
        return stack

