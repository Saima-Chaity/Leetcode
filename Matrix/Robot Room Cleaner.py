'''Robot Room Cleaner - https://leetcode.com/problems/robot-room-cleaner/

You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where
0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the root that is guaranteed to be empty, and you do not have access to
the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with
the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all
surrounded by a wall.'''


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backTrack(i, j, d):
            visited.add((i, j))
            robot.clean()
            for k in range(4):
                new_direction = (d + k) % 4
                x = i + direction[new_direction][0]
                y = j + direction[new_direction][1]
                if (x, y) not in visited and robot.move():
                    backTrack(x, y, new_direction)
                    go_back()
                robot.turnRight()

        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backTrack(0, 0, 0)



