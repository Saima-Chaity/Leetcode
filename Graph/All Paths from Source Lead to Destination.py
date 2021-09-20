'''All Paths from Source Lead to Destination - https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi,
and two nodes source and destination of this graph, determine whether or not all paths starting from source
eventually, end at destination, that is:

At least one path exists from the source node to the destination node
If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
The number of possible paths from source to destination is a finite number.
Return true if and only if all roads from source lead to destination.

Example 1:
Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
Output: false
Explanation: It is possible to reach and get stuck on both node 1 and node 2.'''

from collections import defaultdict
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)

        def dfs(node, destination):
            if visited[node]:
                return False
            if len(graph[node]) == 0:
                return True if node == destination else False
            visited[node] = True
            for neighbor in graph[node]:
                if not dfs(neighbor, destination):
                    return False
            visited[node] = False
            return True

        visited = [False] * n
        return dfs(source, destination)

