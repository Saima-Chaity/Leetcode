'''Max Network Rank

An infrastructure consisting of n cities from l to n, and m bidirectional roads between them are given.
Roads do not intersect apart from at their start and endpoints
(they can pass through underground tunnels to avoid collisions).

For each pair of cities directly connected by a road, let’s define their network rank as the total number of roads
that are connected to either of the two cities.

Write a function, given two arrays starts, ends consisting of m integers each and an integer n, where starts[i]
and ends[i] are cities at the two ends of the i-th road, returns the maximal network rank in the whole infrastructure.

Example:
Input:
starts = [1, 2, 3, 3]
ends = [2, 3, 1, 4]
n = 4
Output:
4'''

def max_network_rank(starts: [int], ends: [int], n: int) -> int:
        graph = [0] * (n+1)
        for a, b in zip(starts, ends):
            graph[a] += 1
            graph[b] += 1

        result = 0
        for a, b in zip(starts, ends):
            value = graph[a] + graph[b] - 1
            result = max(value, result)
        return result

print(max_network_rank([1, 2, 3, 3], [2, 3, 1, 4], 4))
