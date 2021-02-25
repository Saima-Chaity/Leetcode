'''Reconstruct Itinerary - https://leetcode.com/problems/reconstruct-itinerary/

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the
itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when
read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
But it is larger in lexical order.'''

from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def dfs(origin):
            nodeList = groups[origin]
            while nodeList:
                nextNode = nodeList.pop()
                dfs(nextNode)
            output.append(origin)

        groups = defaultdict(list)
        for index, ticket in enumerate(tickets):
            groups[ticket[0]].append(ticket[1])

        for key, value in groups.items():
            groups[key] = sorted(value, reverse=True)

        output = []
        dfs("JFK")
        output = output[::-1]
        return output



#Backtracking
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def dfs(origin, route):
            if len(route) == length + 1:
                self.output = route
                return True
            for index, node in enumerate(groups[origin]):
                if not visited[origin][index]:
                    visited[origin][index] = True
                    result = dfs(node, route + [node])
                    visited[origin][index] = False
                    if result:
                        return True
            return False

        groups = defaultdict(list)
        for index, ticket in enumerate(tickets):
            groups[ticket[0]].append(ticket[1])

        visited = {}
        for key, value in groups.items():
            groups[key] = sorted(value)
            visited[key] = [False] * len(value)

        route = ["JFK"]
        self.output = []
        length = len(tickets)
        dfs("JFK", route)
        return self.output
