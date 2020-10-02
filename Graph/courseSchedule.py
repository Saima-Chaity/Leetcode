# Course Schedule - https://leetcode.com/problems/course-schedule/
'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is
expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.'''

from collections import deque
from collections import defaultdict
# Topologyical sort - DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 0 = unvisited, 1 = visiting, 2 = visited
        
        self.edges = defaultdict(list)
        self.visited = [False] * numCourses
        for course, pre_course in prerequisites:
            self.edges[pre_course].append(course)

        for course in range(numCourses):
            if not self.dfs(course):
                return False
        return True
    
    def dfs(self, course):
        if self.visited[course] == 1: # Already visited node that means there is cycle in the graph
            return False
        if self.visited[course] == 2:
            return True
        self.visited[course] = 1
        for neighbor in self.edges[course]:
            if not self.dfs(neighbor):
                return False
        self.visited[course] = 2
        return True


# Topologyical sort - BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        degree = [0] * numCourses
        for course, pre_course in prerequisites:
            edges[pre_course].append(course)
            degree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if not degree[course]:
                queue.append(course)
        
        courseCount = 0
        while queue:
            course = queue.popleft()
            courseCount += 1
            for next_course in edges[course]:
                degree[next_course] -= 1
                if not degree[next_course]:
                    queue.append(next_course)
        return courseCount == numCourses


# Course Schedule II - https://leetcode.com/problems/course-schedule-ii/
'''There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed 
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take 
to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, 
return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
course 0. So the correct course order is [0,1] .'''

# Topologyical sort - DFS
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0 = unvisited, 1 = visiting, 2 = visited
        
        self.edges = defaultdict(list)
        self.visited = [False] * numCourses
        self.courseOrder = []
        for course, pre_course in prerequisites:
            self.edges[pre_course].append(course)

        for course in range(numCourses):
            if not self.dfs(course):
                return []
        return self.courseOrder
    
    def dfs(self, course):
        if self.visited[course] == 1:
            return False
        if self.visited[course] == 2:
            return True
        self.visited[course] = 1
        for neighbor in self.edges[course]:
            if not self.dfs(neighbor):
                return False
        self.visited[course] = 2
        self.courseOrder.insert(0, course)
        return True


# Topologyical sort - BFS
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        degree = [0] * numCourses
        for course, pre_course in prerequisites:
            edges[pre_course].append(course)
            degree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if not degree[course]:
                queue.append(course)
        
        courseOrder = []
        while queue:
            course = queue.popleft()
            courseOrder.append(course)
            for next_course in edges[course]:
                degree[next_course] -= 1
                if not degree[next_course]:
                    queue.append(next_course)
        return courseOrder if len(courseOrder) == numCourses else []



# Course Schedule III - https://leetcode.com/problems/course-schedule-iii/
'''There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. 
A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.
Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

Note:

The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.'''

import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses = sorted(courses, key = lambda x:x[1])
        heap = []
        time = 0
        for i in range(len(courses)):
            time += courses[i][0]
            heapq.heappush(heap, (-courses[i][0]))
            if time > courses[i][1]:
                time += heapq.heappop(heap)
        return len(heap)
        