''' Race Car - https://leetcode.com/problems/race-car/

Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions.
Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3,
and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.

Example 1:

Input: target = 3
Output: 2
Explanation:
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.'''

# Time complexity - log(target)
from collections import deque
class Solution:
    def racecar(self, target: int) -> int:

        q = deque([(0, 1, 0)])
        while q:
            position, speed, steps = q.popleft()
            if position + speed == target:
                return steps + 1
            q.append((position + speed, speed * 2, steps + 1))
            if speed > 0 and position + speed > target:
                q.append((position, -1, steps + 1))
            if speed < 0 and position + speed < target:
                q.append((position, 1, steps + 1))
        return 0