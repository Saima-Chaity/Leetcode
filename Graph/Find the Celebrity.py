'''Find the Celebrity - https://leetcode.com/problems/find-the-celebrity/

Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity.
The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do
is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out
the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B.
Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party.
Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Example 1:

Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j,
otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1
because both 0 and 2 know him but 1 does not know anybody.'''


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
class Solution:
    def findCelebrity(self, n: int) -> int:

        def isCelebrity(i):
            for j in range(0, n):
                if i == j:
                    continue
                if knows(i, j) or not knows(j, i):
                    return False
            return True

        for i in range(n):
            if isCelebrity(i):
                return i
        return -1


# Using cache and deduct nested loop
from functools import lru_cache
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
class Solution:
    def findCelebrity(self, n: int) -> int:

        @lru_cache(maxsize=None)
        def cachedKnows(a, b):
            return knows(a, b)

        def isCelebrity(i):
            for j in range(0, n):
                if i == j:
                    continue
                if cachedKnows(i, j) or not cachedKnows(j, i):
                    return False
            return True

        celebrityCandidate = 0
        cache = {}
        for i in range(1, n):
            result = cachedKnows(celebrityCandidate, i)
            if result:
                celebrityCandidate = i
        if isCelebrity(celebrityCandidate):
            return celebrityCandidate
        return -1