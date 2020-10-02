# Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/
'''You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, 
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.'''

from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                graph[i].append((cost, j))
                graph[j].append((cost, i))
        
        seen = [0] * (len(points)+1)
        seen[0] = 1
        q = graph[0]
        minimumCost = 0
        connectedNodes = 1
        heapq.heapify(q)
        while q:
            cost, point = heapq.heappop(q)
            if not seen[point]:
                seen[point] = 1
                minimumCost += cost
                connectedNodes += 1
                for connectingCost, neighbour in graph[point]:
                    heapq.heappush(q, (connectingCost, neighbour))
            if connectedNodes >= len(points):
                break
        return minimumCost


#Kruskal's Algorithm
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        cost_map = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                cost_map[(i, j)] = cost
        
        graph = []
        for key, value in cost_map.items():
            graph.append([key[0], key[1], value])        
        
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
        parent = {city:city for city in range(0, len(points))}
        #Sort connections so we are always picking minimum cost edge.
        graph.sort(key=lambda x:x[2])
        totalCost = 0
        for city1, city2, cost in graph:
            if union(city1, city2):
                totalCost += cost
        
        # Check that all cities are connected
        root = find(len(points)-1)
        for i in range(0, len(points)):
            if find(i) == root:
                continue
            else:
                return -1
        return totalCost