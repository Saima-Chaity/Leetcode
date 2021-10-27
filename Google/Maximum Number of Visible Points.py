'''Maximum Number of Visible Points - https://leetcode.com/problems/maximum-number-of-visible-points/

You are given an array points, an integer angle, and your location, where location = [posx, posy]
and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move from your position,
but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees
is represented by angle, determining how wide you can see from any given view direction. Let d be
the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive
range of angles [d - angle/2, d + angle/2].


You can see some set of points if, for each point, the angle formed by the point, your position,
and the immediate east direction from your position is in your field of view.

There can be multiple points at one coordinate. There may be points at your location, and you can
always see these points regardless of your rotation. Points do not obstruct your vision to other points.

Return the maximum number of points you can see.

Example 1:

Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3
Explanation: The shaded region represents your field of view. All points can be made visible in your field of view,
including [3,3] even though [2,2] is in front and in the same line of sight.
'''

import math
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:

        array = []
        same_coordinate = 0
        for point in points:
            if point == location:
                same_coordinate += 1
            else:
                array.append(math.degrees(math.atan2(point[1] - location[1], point[0] - location[0])))

        array.sort()
        angles = array + [item + 360 for item in array]
        left = 0
        max_visible_points = 0
        for right, currentAngle in enumerate(angles):
            if currentAngle - angles[left] > angle:
                left += 1
            max_visible_points = max(max_visible_points, right - left + 1)
        return max_visible_points + same_coordinate

