from collections import defaultdict
import heapq
class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, src):
        distance = [float('inf') for _ in range(self.v)]
        distance[src] = 0
        heap = []
        visited = set()
        for v in range(self.v):
            visited.add(v)
            heapq.heappush(heap, (v, distance[v]))

        parent = [-1] * self.v
        while heap:
            u = heapq.heappop(heap)[0]
            visited.discard(v)
            for neighbor, weight in self.graph[u]:
                if neighbor in visited and weight < distance[neighbor]:
                    distance[neighbor] = weight
                    parent[neighbor] = u
                    heapq.heappush(heap, (neighbor, distance[neighbor]))

        for node in range(1, self.v):
            print(parent[node], "->", node)

graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijkstra(0)