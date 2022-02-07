# Task Scheduler - https://leetcode.com/problems/task-scheduler/
'''Given a characters array tasks, representing the tasks a CPU needs to do, where each letter
represents a different task. Tasks could be done in any order. Each task is done in one unit of time.
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.'''

# Time complexity - 0(n)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        frequencies = [0] * 26
        for task in tasks:
            frequencies[ord(task) - ord('A')] += 1

        frequencies.sort()
        max_freq = frequencies.pop()
        idle_time = (max_freq - 1) * n
        while frequencies and idle_time > 0:
            idle_time -= min(max_freq - 1, frequencies.pop())

        idle_time = max(0, idle_time)
        return len(tasks) + idle_time


from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        taskCounts = Counter(tasks)
        heap = []
        for task, count in taskCounts.items():
            heapq.heappush(heap, (-count, task))

        taskCount = 0
        while heap:
            coolingPeriod, tempTaskHolder = -1, []
            while coolingPeriod < n:
                if heap:
                    count, task = heapq.heappop(heap)
                    coolingPeriod += 1
                    taskCount += 1
                    if count != -1:
                        tempTaskHolder.append((count + 1, task))
                else:
                    if tempTaskHolder:
                        taskCount += (n - coolingPeriod)
                    break

            for item in tempTaskHolder:
                heapq.heappush(heap, (item))
        return taskCount


