'''Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

We want to split a group of n people (labeled from 1 to n) into two groups of any size.
Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled
ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false'''

from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        def checkBipartite(node, color):
            seen[node] = color
            for neighbor in graph[node]:
                if neighbor in seen and seen[neighbor] == seen[node]:
                    return False
                if neighbor not in seen:
                    if seen[node] == 'blue':
                        if not checkBipartite(neighbor, 'red'):
                            return False
                    else:
                        if not checkBipartite(neighbor, 'blue'):
                            return False
            return True

        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        seen = {}
        for i in range(len(graph)):
            if i not in seen:
                if not checkBipartite(i, 'blue'):
                    return False
        return True

