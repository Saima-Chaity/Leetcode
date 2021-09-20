'''Parallel Courses- https://leetcode.com/problems/parallel-courses/

You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given
an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship
between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous
semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses,
return -1.

Example 1:

Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.'''

from collections import defaultdict, deque
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        edges = defaultdict(list)
        degree = defaultdict(int)
        for pre_course, course in relations:
            edges[pre_course].append(course)
            degree[course] += 1

        queue = deque()
        for course in range(1, n + 1):
            if not degree[course]:
                queue.append(course)

        semester_count = 0
        studied_count = 0
        while queue:
            new_queqe = deque()
            semester_count += 1
            for _ in range(len(queue)):
                studied_count += 1
                course = queue.popleft()
                for next_course in edges[course]:
                    degree[next_course] -= 1
                    if not degree[next_course]:
                        new_queqe.append(next_course)
            queue = new_queqe
        return semester_count if studied_count == n else -1