from collections import defaultdict
import heapq
class Solution:
  def minimumCostToConnectNodes(self, n, edges, newEdges):

      cost_map = {}

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

      def find(city):
          if parent[city] != city:
              parent[city] = find(parent[city])
          return parent[city]

      def union(city1, city2):
          root1 = find(city1)
          root2 = find(city2)
          if root1 == root2:
              return False  # Cycle
          parent[root2] = root1  # Join roots
          return True

      # Keep track of disjoint sets. Initially each city is its own set.
      parent = {city: city for city in range(1, n + 1)}
      # Sort connections so we are always picking minimum cost edge.
      connections.sort(key=lambda x: x[2])
      totalCost = 0
      for city1, city2, cost in connections:
          if union(city1, city2):
              totalCost += cost

      # Check that all cities are connected
      root = find(n)
      for i in range(1, n + 1):
          if find(i) == root:
              continue
          else:
              return -1
      return totalCost


print(Solution.minimumCostToConnectNodes((),6, [[1, 4], [4, 5], [2, 3]], [[1, 2, 5], [1, 3, 10],
                                                                          [1, 6, 2], [5, 6, 5]])) #7
print(Solution.minimumCostToConnectNodes((),5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],
                                         [[1, 2, 12], [3, 4, 30], [1, 5, 8]])) # 20
print(Solution.minimumCostToConnectNodes((),6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]],
                                         [[1, 6, 410], [2, 4, 800]])) # 410
print(Solution.minimumCostToConnectNodes((),6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
                         [[1, 5, 110], [2, 4, 84], [3, 4, 79]])) # 79




