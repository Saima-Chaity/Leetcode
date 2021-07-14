'''Widest Path Without Trees

There are N trees (numbered from 0 to N-1) in a forest. The K-th tree is located at coordinates (X[K], Y[K]).
We want to build the widest possible vertical path, such that there is no tree on it. The path must be built
somewhere between a leftmost and a rightmost tree, which means that the width of the path cannot be infinite.

What is the width of the widest possible path that can be built?

Write a function:

def solution(X, Y)
that, given two arrays X and Y consisting of N integers each, denoting the positions of trees, returns the
widest possible path that can be built.

Example 1:
Input: X = [5,5,5,7,7,7], Y=[3,4,5,1,3,7]

Output: 2
'''

def widest_path(x: [int], y: [int]) -> int:
    difference = 0
    x = sorted(x)
    for i in range(len(x) - 1):
        diff = x[i + 1] - x[i]
        if diff > difference:
            difference = diff
    return difference