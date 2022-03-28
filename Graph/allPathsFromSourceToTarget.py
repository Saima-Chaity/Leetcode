# All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/
'''Given a directed acyclic graph of N nodes. Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example 1:

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def backTrack(node, path):
            if node == len(graph) - 1:
                output.append(path)
                return
            for neighbor in graph[node]:
                visited[node] = True
                backTrack(neighbor, path + [neighbor])
                visited[node] = False

        output = []
        visited = [False] * len(graph)
        backTrack(0, [0])
        return output