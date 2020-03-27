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


# Min Cost to Connect All Nodes
'''Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects 
nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect 
all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each 
other.

Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7'''

from collections import defaultdict
import heapq

#Prim's algorithm
class Solution:
  def minimumCostToConnectNodes(self, n, edges, newEdges) -> int:

    neighbors = defaultdict(list)
    addedEdges = set()

    for node1, node2, cost in newEdges:
      neighbors[node1].append((cost, node2))
      neighbors[node2].append((cost, node1))
      addedEdges.add((node1, node2))
      addedEdges.add((node2, node1))

    for node1, node2 in edges:
      if (node1, node2) not in addedEdges:
        neighbors[node1].append((0, node2))
        neighbors[node2].append((0, node1))

    q = [(0, 1)]
    visited = set()
    minCost = 0

    while q:
      cost, node = heapq.heappop(q)
      if node not in visited:
        visited.add(node)
        minCost += cost

        for cost, connectedNode in neighbors[node]:
          heapq.heappush(q, (cost, connectedNode))
    return minCost

#Kruskal's Algorithm
  def minimumCostToConnectNodes1(self, n, edges, newEdges) -> int:

    memo = {}
    cost_map = {}

    def find(node):
      memo.setdefault(node, node)
      if memo[node] == node:
        return node
      else:
        return find(memo[node])

    def union(node1, node2):
      node1Value, node2Value = find(node1), find(node2)
      if node1Value != node2Value:
        memo[node1Value] = node2Value
        return nodes-1, totalCost+cost
      return nodes, totalCost


    for node1, node2, cost in newEdges:
      cost_map[(node1, node2)] = cost

    for node1, node2 in edges:
      if (node1, node2) not in cost_map:
        cost_map[(node1, node2)] = 0

    connections = []

    for key in cost_map:
      node1, node2 = key
      connections.append([node1, node2, cost_map[key]])

    if len(connections) < n - 1:
      return -1

    if n == 1:
      return 0

    connections.sort(key=lambda x: x[2])
    totalCost = 0
    nodes = n - 1

    for node1, node2, cost in connections:
      nodes, totalCost = union(node1, node2)

    return totalCost if nodes == 0 else - 1

print(Solution.minimumCostToConnectNodes1((),6, [[1, 4], [4, 5], [2, 3]], [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))
print(Solution.minimumCostToConnectNodes1((),5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
print(Solution.minimumCostToConnectNodes1((),6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], [[1, 6, 410], [2, 4, 800]]))
print(Solution.minimumCostToConnectNodes1((),6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
                         [[1, 5, 110], [2, 4, 84], [3, 4, 79]]))


# Number of Operations to Make Network Connected - https://leetcode.com/problems/number-of-operations-to-make-network-connected/
'''There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where 
connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer 
directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, 
and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of 
times you need to do this in order to make all the computers connected. If it's not possible, return -1. '''

# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1

from collections import defaultdict
import heapq

class Solution:
  def makeConnected(self, n, connections) -> int:
    if len(connections) < n - 1:
      return -1

    neighbors = defaultdict(list)
    for connection1, connection2 in connections:
      neighbors[connection1].append(connection2)
      neighbors[connection2].append(connection1)

    def dfs(node):
      if not visited[node]:
        visited[node] = 1
        for neighborComponent in neighbors[node]:
          dfs(neighborComponent)

    visited = [0] * n
    numOfOperations = 0

    for i in range(n):
      if not visited[i]:
        dfs(i)
        numOfOperations += 1
    return numOfOperations - 1