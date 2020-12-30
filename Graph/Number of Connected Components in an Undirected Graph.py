'''Number of Connected Components in an Undirected Graph -
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1'''

from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        q = deque()
        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                q.append(i)
                while q:
                    node = q.popleft()
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            q.append(neighbour)
                            visited.add(neighbour)
                    del graph[node]
                count += 1
        return count
