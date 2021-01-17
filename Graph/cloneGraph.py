# Clone Graph - https://leetcode.com/problems/clone-graph/
'''Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
'''

from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        q = deque([node])
        visited = {}
        visited[node] = Node(node.val, [])

        while q:
            oldNode = q.popleft()
            for neighbour in oldNode.neighbors:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited[neighbour] = Node(neighbour.val, [])
                visited[oldNode].neighbors.append(visited[neighbour])
        return visited[node]


#DFS
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clonedNode = Node(node.val, [])
        self.visited[node] = clonedNode
        if node.neighbors:
            clonedNode.neighbors = [self.cloneGraph(neighbour) for neighbour in node.neighbors]
        return clonedNode