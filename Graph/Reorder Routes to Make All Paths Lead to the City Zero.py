'''Reorder Routes to Make All Paths Lead to the City Zero
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two
different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads
in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum
number of edges changed.

It's guaranteed that each city can reach the city 0 after reorder.

Example 1:

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).'''

#BFS
from collections import defaultdict, deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        graph = defaultdict(list)
        for src, dest in connections:
            graph[src].append((dest, 1))
            graph[dest].append((src, 0))

        reorderRoutes = 0
        q = deque([0])
        visited = set()
        visited.add(0)

        while q:
            node = q.popleft()
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    reorderRoutes += cost
                    visited.add(neighbor)
                    q.append(neighbor)
        return reorderRoutes


#DFS
from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        incoming = defaultdict(list)
        outgoing = defaultdict(list)
        for src, dest in connections:
            outgoing[src].append(dest)
            incoming[dest].append(src)

        reorderRoutes = 0
        stack = [0]
        visited = set()
        visited.add(0)

        while stack:
            node = stack.pop()
            for neighbor in incoming[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
            for neighbor in outgoing[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    reorderRoutes += 1
            visited.add(node)
        return reorderRoutes

