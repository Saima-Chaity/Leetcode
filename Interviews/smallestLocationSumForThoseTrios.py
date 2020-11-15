'''Uber is trying to assess customer route patters and offer suggestions to other user based on this. 
Each from and to for a route can be represented as an undirected edge. A group of n locations is 
uniquely numbered from 1 to n. A trio is defined as a group of 3 related locations that call connected by an edge.
Trios are scored by counting the number of related locations outside of the trio, this is referred to as location sum.

Given location relation data, determine the minimum location sum for all trios of related locations in the group, if no such trio return -1

Example input:
location_nodes = 6
location_edges = 6
from = [1,2,2,3,4,5]
to = [2,4,5,5,5,6]

Undirected Edges are basically from[i] to to[i] for each i and vice versa since they are undirected

Example output
Answer is 3
Explanation: The trio here is [2,4,5] and location sum for it is 3 becaue 2 is connected to 1 outside of trio 
and 3 is connected to 5 outside of trio and 6 is connected to 4 outside of trio. So a total of 3 connected 
locations outside of the trio.

If there are multiples trios, return the smallest location sum for those trios'''


def getMinLocationSum(node_from, node_to):
    visited = set()
    minLocationSum = float('inf')
    graph = {}

    for i, j in zip(node_from, node_to):
        graph[i], graph[j] = graph.get(i, set()), graph.get(j, set())
        graph[i].add(j)
        graph[j].add(i)
    
    for node in graph: # Start with a node
        neighbours = graph[node] # Find the neighbors of that node
        for neighbour in neighbours: # For each of the neighbors...
            neighbour_neighbours = graph[neighbour]  # Find the neighbors of the neighbor
            shared_neighbors = neighbour_neighbours.intersection(neighbours) # Get the shared neighbors which are trios
            if shared_neighbors:
                for shared_neighbor in shared_neighbors:
                    trio = tuple(sorted([node, neighbour, shared_neighbor]))
                    if trio not in visited:
                        visited.add(trio)
                        degree = len(neighbours) + len(neighbour_neighbours) + len(graph[shared_neighbor])
                        locationSum = degree - 6
                        if locationSum < minLocationSum:
                            minLocationSum = locationSum
    return minLocationSum if minLocationSum != float('inf') else -1

getMinLocationSum([1,1,2,2,3,4], [2,3,3,4,4,5]) # Returns 2
getMinLocationSum([1,2,2,3,4,5], [2,4,5,5,5,6]) # Returns 3
getMinLocationSum([1], [2]) # Returns -1 