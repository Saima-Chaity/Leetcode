# High Five - https://leetcode.com/problems/high-five/

'''Given a list of scores of different students, return the average score of each student's top five scores in the order 
of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated 
using integer division.

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
'''

import heapq
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        student = defaultdict(list)
        output = []
        for item in items:
            heapq.heappush(student[item[0]], item[1])
            if len(student[item[0]]) > 5:
                heapq.heappop(student[item[0]])

        for key in student.keys():
            studentWithAverage = sum(student[key]) // 5
            output.append([key, studentWithAverage])

        return output
