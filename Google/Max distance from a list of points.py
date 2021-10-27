'''Max distance from a list of points

Given N points on an axis x1, x2, x3, …, xN where (0 < x1 < x2 < … < xN).
Each point i has a value p_i.

(1) Find a pair (i, j) that maximize p_i + p_j + |x_i - x_j|.

Example:
Points: [0, 3, 6]
Values: [-5, 4, 7]
Return: Either the point pair of (3, 6) or (6, 6)
Reasoning is that for these two points, p_i + p_j + |x_i - x_j| = 14

Full evaluation of the example above with (Point pairs) -> result

0, 0 -> (-5 + -5) + (0 - 0)= -10
0, 3 -> (-5 + 4) + (3 - 0) = 2
0, 6 -> (-5 + 7) + (6 - 0) = 4
3, 3 -> (4 + 4) + (3 - 3) = 8
3, 6 -> (4 + 7) + (6 - 3) = 14
6, 6 -> (7 + 7) + (6 - 6) = 14
'''

class Solution:
    def findMaxValueOfEquation(points, values) -> int:

        ''' Notice that the positions are given in sorted order, 0<x1<x2<x3..
        We have to maximize expression pi + pj + |xi-xj|
        //Now as the positions are sorted and are all positive, |xi-xj| will always evaluate to (xj-xi) if j>i
        //So the expression becomes, pi + pj + (xj-xi) for j>i
        //This is equal to (pi - xi) + (pj + xj)

        //Now we can maintain a max variable for the value pi - xi
        //And keep on updating answer for each j
        Below is the code'''

        maxValue = points[0] - values[0]
        answer = 0
        for i in range(1, len(points)):
            value = points[i] + values[i]
            answer = max(answer, maxValue + value)
            maxValue = max(maxValue, points[i] - values[i])

        return answer


print(Solution.findMaxValueOfEquation([-5, 4, 7], [0, 3, 6]))