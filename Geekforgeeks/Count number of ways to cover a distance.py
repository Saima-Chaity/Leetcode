'''
Count number of ways to cover a distance
Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.

Examples:

Input: n = 3
Output: 4
Explantion:
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input: n = 4
Output: 7
Explantion:
Below are the four ways
 1 step + 1 step + 1 step + 1 step
 1 step + 2 step + 1 step
 2 step + 1 step + 1 step
 1 step + 1 step + 2 step
 2 step + 2 step
 3 step + 1 step
 1 step + 3 step
'''

def printCountDP(distance):
    mapping = [0] * (distance+1)
    mapping[0] = 1
    mapping[1] = 1
    mapping[2] = 2
    for i in range(3, distance+1):
        mapping[i] = mapping[i-1] + mapping[i-2] + mapping[i-3]
    return mapping[distance]

dist = 4;
print(printCountDP(dist))