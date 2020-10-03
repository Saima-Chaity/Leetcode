# Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find 
the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.'''

from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v,w))
        
        distance = [float('inf') for _ in range(n)]
        q = [(-1, src, 0)]
        
        while q:
            stops, source, price = heapq.heappop(q)
            if source == dst or stops == K:
                continue

            for neighbour, cost in graph[source]:
                if price + cost >= distance[neighbour]:
                    continue
                else:
                    distance[neighbour] = price + cost
                    heapq.heappush(q, (stops+1, neighbour, price + cost))
        return distance[dst] if distance[dst] < float('inf')  else -1