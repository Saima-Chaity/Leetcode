'''Minimum Area Rectangle - https://leetcode.com/problems/minimum-area-rectangle/

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes.
If there is not any such rectangle, return 0.

Example 1:
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
'''

from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        # Sort in such way that [1,1] precedes [2, 2], and [2, 2] precedes [2, 3]
        points.sort(key=lambda x: (x[0], x[1]))
        # Create a map that stores all Y co-ords for all X co-ords
        # [1, 2], [1, 3] becomes {1: (2, 3)}
        xy_coordinates = defaultdict(set)
        for point in points:
            xy_coordinates[point[0]].add(point[1])

        # For each (X1, Y1) find (X2, Y2) as the co-ordinates of the anti-diagonal
        min_area = float('inf')
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i + 1, len(points)):
                x2 = points[j][0]
                y2 = points[j][1]
                # Diagonal co-ordinates can never be equal
                if x1 == x2 or y1 == y2:
                    continue
                # Once we have a valid set of diagonal co-ordinates
                # We can check if we can find a complete set of 4 co-ordinates
                if y2 in xy_coordinates[x1] and y1 in xy_coordinates[x2]:
                    min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))
        return min_area if min_area != float('inf') else 0