# Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/
'''Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and
there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges
denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such
that the edge colors alternate along the path (or -1 if such a path doesn't exist).

Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]'''

from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:

        graph = {i: [[], []] for i in range(n)}

        for [i, j] in red_edges:
            graph[i][0].append(j)
        for [i, j] in blue_edges:
            graph[i][1].append(j)

        result = [float('inf') for _ in range(n)]
        result[0] = 0
        minLength = 0

        visited = set()
        q = deque()
        q.append((0, "r"))
        q.append((0, "b"))

        while q:
            qLength = len(q)
            minLength += 1
            for _ in range(qLength):
                node, color = q.popleft()
                if (node, color) not in visited:
                    visited.add((node, color))
                    if color == 'r':
                        for child in graph[node][1]:
                            q.append((child, 'b'))
                            result[child] = min(minLength, result[child])
                    if color == 'b':
                        for child in graph[node][0]:
                            q.append((child, 'r'))
                            result[child] = min(minLength, result[child])
        for i in range(n):
            if result[i] == float('inf'):
                result[i] = -1
        return result
