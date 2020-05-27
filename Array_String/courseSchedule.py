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


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course = {i: set() for i in range(numCourses)}
        preCourse = defaultdict(set)

        for i, j in prerequisites:
            course[i].add(j)
            preCourse[j].add(i)

        queue = deque([])
        for key, value in course.items():
            if len(value) == 0:
                queue.append(key)

        while queue:
            item = queue.popleft()
            for i in preCourse[item]:
                course[i].remove(item)
                if len(course[i]) == 0:
                    queue.append(i)
            course.pop(item)
        return len(course) == 0



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

from collections import defaultdict
class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj_list = defaultdict(list)
        indegree = {}
        for i, j in prerequisites:
            adj_list[j].append(i)
            indegree[i] = indegree.get(i, 0) + 1

        zero_indegree_queue = [k for k in range(numCourses) if k not in indegree]
        topological_sorted_order = []

        while zero_indegree_queue:
            vertex = zero_indegree_queue.pop(0)
            topological_sorted_order.append(vertex)
            if vertex in adj_list:
                for i in adj_list[vertex]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        zero_indegree_queue.append(i)
        return topological_sorted_order if len(topological_sorted_order) == numCourses else []