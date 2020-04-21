from collections import defaultdict
import heapq

class Solution:
    def minCostForRepair(n, edges, edgesToRepair):
        graph = defaultdict(list)
        addedEdges = set()

        for city1, city2, cost in edgesToRepair:
            graph[city1].append((cost, city2))
            graph[city2].append((cost, city1))
            addedEdges.add((city1, city2))
            addedEdges.add((city2, city1))

        for city1, city2 in edges:
            if (city1, city2) not in addedEdges:
                graph[city1].append(((0, city2)))
                graph[city2].append((0, city1))

        q = [(0, 1)]
        visited = set()
        totalCost = 0

        while q:
            cost, city = heapq.heappop(q)
            if city not in visited:
                visited.add(city)
                totalCost += cost
                for cost, connectedCity in graph[city]:
                    if connectedCity not in visited:
                        heapq.heappush(q, (cost, connectedCity))
        return totalCost

print(Solution.minCostForRepair(6, [[1, 4], [4, 5], [2, 3]], [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))

print(Solution.minCostForRepair(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
print(Solution.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], [[1, 6, 410], [2, 4, 800]]))
print(Solution.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
                         [[1, 5, 110], [2, 4, 84], [3, 4, 79]]))