'''Shopping Patterns

A Company is trying to understand customer shopping patterns and offer items that are regularly
bought together to new customers. Each item that has been bought together can be represented as
an undirected graph where edges join often bundled products. A group of n products is uniquely
numbered from 1 of product_nodes. A trio is defined as a group of three related products that
all connected by an edge. Trios are scored by counting the number of related products outside
of the trio, this is referred as a product sum.

Given product relation data, determine the minimum product sum for all trios of related products
in the group. If no such trio exists, return -1.

Input
The input to the function/method consists of four arguments:

int products_nodes: the total number of products

int products_edges: the total number of edges representing related products

int products_from[products_nodes]: each element is a node of one side of an edge.

int products_to[products edges]: each products_to[i] is a node connected to products_from[i]

Output
int: the minimum product sum for all trios of related products in the group. If no such trio exists,
return -1.

Constraints
1 <= products_nodes <= 500
1 <= products_edges <= min(500, (products_nodes * (products_nodes - 1)) / 2)
1 <= products_from[i], products to[i] <= products_nodes
products_from[i] != products_to[i]
Examples
Example 1:
Input:
products_nodes = 6

`products_edges = 6

products_from = [1, 2, 2, 3, 4, 5]

products_to = [2, 4, 5, 5, 5, 6]

Product	Related Products
1	2
2	1,4,5
3	5
4	2,5
5	2,3,4,6
6	5


A graph of n = 6 products where the only trio of related products is (2, 4, 5).

Product	Outside Products	Which Products Are Outside
2	1	1
4	0
5	2	3,6
In the diagram above, the total product score is 1 + 0 + 2 = 3 for the trio (2, 4, 5).

Output: 3
Example 2:
Input:
products_nodes = 5

products_edges = 6

products_from = [1, 1, 2, 2, 3, 4]

products_to = [2, 3, 3, 4, 4, 5]

Output: 2
Explanation:
There are two possible trios: {1,2,3} and {2,3,4}

The score for {1,2,3} is 0 + 1 + 1 = 2.

The score for {2,3,4} is 1 + 1 + 1 = 3.
Return 2.
'''

from collections import defaultdict
class Solution:
    def shoppingPatterns(self, products_nodes, products_edges, products_from, products_to):

        def dfs(start, current, graph, visited, score, edge):
            nonlocal minimum
            visited[current] = True
            neighbors = graph[current]
            currentScore = len(neighbors) - edge
            totalScore = currentScore + score
            for node in neighbors:
                if edge == 3:
                    if node == start:
                        minimum = min(minimum, totalScore)
                else:
                    dfs(start, node, graph, visited, totalScore, edge+1)
            visited[current] = False

        graph = defaultdict(list)
        for i in range(products_edges):
            graph[products_from[i]].append(products_to[i])
            graph[products_to[i]].append(products_from[i])

        visited = [False] * (products_nodes+1)
        minimum = float('inf')
        for i in range(products_nodes+1):
            if i in graph:
                dfs(i, i, graph, visited, 0, 1)
        return minimum if minimum != float('inf') else -1



products_nodes = 5
products_edges = 6
products_from = [1, 1, 2, 2, 3, 4]
products_to = [2, 3, 3, 4, 4, 5]
print(Solution.shoppingPatterns((), products_nodes, products_edges, products_from, products_to)) # 2

products_nodes = 6
products_edges = 6
products_from = [1, 2, 2, 3, 4, 5]
products_to = [2, 4, 5, 5, 5, 6]
print(Solution.shoppingPatterns((), products_nodes, products_edges, products_from, products_to)) # 3