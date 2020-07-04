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
        if self.visited[course] == 1:
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