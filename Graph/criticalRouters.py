'''You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which,
when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of
connected components in the graph). The task is to find all articulation points in the given graph.

Input:
The input to the function/method consists of three arguments:

numNodes, an integer representing the number of nodes in the graph.
numEdges, an integer representing the number of edges in the graph.
edges, the list of pair of integers - A, B representing an edge between the nodes A and B.

Output:
Return a list of integers representing the critical nodes.

Example:

Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
Output: [2, 3, 5]
'''

from collections import defaultdict
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """

        self.parent = {i: -1 for i in range(n)}
        self.discoveryTime = {}
        self.lowTime = {}
        self.visited = set()
        self.time = 1
        self.criticalConnection = []

        self.edges = defaultdict(list)
        for u, v in connections:
            self.edges[u].append(v)
            self.edges[v].append(u)

        self.dfs(0)
        return self.criticalConnection

    def dfs(self, node):
        self.discoveryTime[node] = self.time
        self.lowTime[node] = self.time
        self.time += 1
        self.visited.add(node)

        for child in self.edges[node]:

            # moving forward
            if child not in self.visited:
                self.parent[child] = node
                self.dfs(child)

                # update lowTime of parent
                # Check if the subtree rooted with child has a connection to
                # one of the ancestors of node
                self.lowTime[node] = min(self.lowTime[node], self.lowTime[child])

                # If the lowest vertex reachable from subtree
                # under child is below node in DFS tree, then child-node is a bridge
                # this condition checks for bridge or not
                if self.lowTime[child] > self.discoveryTime[node]:  # bridge condition
                    # self.cri_conn.append([child, node])
                    self.criticalConnection.append(node)

            # back edges exists meaning check any early nodes exists
            # if it is update the lowTime of parent node
            elif child != self.parent[node]:
                self.lowTime[node] = min(self.lowTime[node], self.discoveryTime[child])


obj = Solution()
print(obj.criticalConnections(7, [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]))