# Connecting Cities With Minimum Cost - https://leetcode.com/problems/connecting-cities-with-minimum-cost/
'''There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and
city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that
connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.'''

# Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
# Output: 6

from collections import defaultdict
import heapq

class Solution:
  def minimumCost(self, N, connections) -> int:

    neighbors = defaultdict(list)
    for i, j, cost in connections:
      neighbors[i].append((cost, j))
      neighbors[j].append((cost, i))

    q = [(0, 1)]
    visited = set()
    minCost = 0

    while q:
      cost, city = heapq.heappop(q)
      if city not in visited:
        visited.add(city)
        minCost += cost

        if len(visited) == N:
          return minCost

        for cost, neighborCity in neighbors[city]:
          heapq.heappush(q, (cost, neighborCity))
    return -1


# Using Dijkstra's Algorithm
from collections import defaultdict
import heapq
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:

        graph = defaultdict(list)
        for city1, city2, cost in connections:
            graph[city1].append((city2, cost))
            graph[city2].append((city1, cost))
        
        seen = [False] * (N+1)
        q = [(0, 1)]
        minimumCost = 0
        connectedCities = 0
        while q:
            cost, city = heapq.heappop(q)
            if seen[city]:
                continue
            seen[city] = True
            minimumCost += cost
            connectedCities += 1
            for neighbour, connectingCost in graph[city]:
                if not seen[neighbour]:
                    heapq.heappush(q, (connectingCost, neighbour))
        return minimumCost if connectedCities == N else -1
    
    
# Kruskal's Algorithm
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        
        def find(city):
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]
        
        def union(city1, city2):
            root1 = find(city1)
            root2 = find(city2)
            if root1 == root2:
                return False # Cycle
            parent[root2] = root1 # Join roots
            return True
            
        #Keep track of disjoint sets. Initially each city is its own set.
        parent = {city:city for city in range(1, N+1)}
        #Sort connections so we are always picking minimum cost edge.
        connections.sort(key=lambda x:x[2])
        totalCost = 0
        for city1, city2, cost in connections:
            if union(city1, city2):
                totalCost += cost
        
        # Check that all cities are connected
        root = find(N)
        for i in range(1, N+1):
            if find(i) == root:
                continue
            else:
                return -1
        return totalCost
    