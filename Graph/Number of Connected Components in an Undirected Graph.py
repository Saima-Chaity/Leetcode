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
                visited.add(i)
                while q:
                    node = q.popleft()
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            q.append(neighbour)
                            visited.add(neighbour)
                count += 1
        return count


# Union-find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def find(parent, node):
            if parent[node] != node:
                parent[node] = find(parent, parent[node])
            return parent[node]

        def union(parent, rank, node1, node2):
            if rank[node1] > rank[node2]:
                parent[node2] = node1
            elif rank[node1] < rank[node2]:
                parent[node1] = node2
            else:
                parent[node2] = node1
                rank[node1] += 1

        parent = [node for node in range(n)]
        rank = [0 for i in range(n)]

        for node1, node2 in edges:
            parentOfNode1 = find(parent, node1)
            parentOfNode2 = find(parent, node2)
            if parentOfNode1 != parentOfNode2:
                union(parent, rank, parentOfNode1, parentOfNode2)

        connection = set()
        for i in range(n):
            connection.add(find(parent, i))
        return len(connection)
