'''You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right.
You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.'''

def avoidObstacles(inputArray):
    inputArray.sort()
    jump = 1
    obstacleHit = True
    while obstacleHit:
        obstacleHit = False
        jump += 1
        for i in range(len(inputArray)):
            if inputArray[i] % jump == 0:
                obstacleHit = True
                break
    return jump

