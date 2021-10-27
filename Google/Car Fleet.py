'''Car Fleet - https://leetcode.com/problems/car-fleet/

There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the
ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car
is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3
'''

'''sort on the start position.
        the car behind can only catch up no exceed.
        so if the car start late and speed is faster, it will catch up and become a fleet.
        but there is a constrain, there is a target.
        so use arrive time to measure. 
        
        start late but arrive ealier means the car behind will catch up before the target.
        
        position  10  8  5  3  0
        distance  2   4  7  9  12
        speed.    2   4  1  3  1
        time.     1   1  7  3  12
                      ^     ^
                      |     |
                     catch  catch up the previous car before target, join the fleet
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        position_speed = zip(position, speed)
        for position, speed in sorted(position_speed, reverse=True):
            distance = (target - position) / speed
            if not stack:
                stack.append(distance)
            elif distance > stack[-1]:
                stack.append(distance)
        return len(stack)
