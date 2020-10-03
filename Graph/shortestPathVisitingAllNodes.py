# Shortest Path Visiting All Nodes - https://leetcode.com/problems/shortest-path-visiting-all-nodes/
'''An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, 
you may revisit nodes multiple times, and you may reuse edges.

Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]'''

from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        def getKey(graph, path, index):
            arr = []
            path = set(path)
            for i in range(len(graph)):
                if i not in path:
                    arr.append(i)
            return (tuple(arr), index)

            
        q = deque()
        visited = set()
        # put the nodes in the queue
        for i in range(len(graph)):
            q.append((i, [i]))
        
        while q:
            qLength = len(q)
            for i in range(qLength):
                node, path = q.popleft()
                # shortest path must be the first which travelled all the nodes
                if len(set(path)) == len(graph):
                    return len(path) - 1
                # explore paths with adjacent nodes
                for child in graph[node]:
                    newPath = path + [child]
                    # use (remaining nodes, current node) as key to avoid redundant calculation
                    key = getKey(graph, newPath, child)
                    if key not in visited:
                        visited.add(key)
                        q.append((child, newPath))
                    else:
                        continue
        return 0