'''Valid Square - https://leetcode.com/problems/valid-square/
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true
Example 2:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false
Example 3:

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true
'''


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1, p2):
            return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0])

        p = [p1, p2, p3, p4]
        p = sorted(p, key=lambda x: (x[0], x[1]))
        return distance(p[0], p[1]) != 0 and distance(p[0], p[1]) == distance(p[1], p[3]) and \
               distance(p[1], p[3]) == distance(p[3], p[2]) and distance(p[3], p[2]) == distance(p[2], p[0]) and \
               distance(p[0],p[3]) == distance(p[1], p[2])


# Another approach
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1, p2):
            return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0])

        def isSame(p1, p2):
            return p1[0] == p2[0] and p1[1] == p2[1]

        resultSet = set()
        if isSame(p1, p2) or isSame(p1, p3) or isSame(p1, p4) or isSame(p2, p3) or isSame(p2, p4) or isSame(p3, p4):
            return False

        resultSet.add(distance(p1, p2))
        resultSet.add(distance(p1, p3))
        resultSet.add(distance(p1, p4))
        resultSet.add(distance(p2, p3))
        resultSet.add(distance(p2, p4))
        resultSet.add(distance(p3, p4))
        return len(resultSet) == 2
