'''Process Restricted Friend Requests
https://leetcode.com/problems/process-restricted-friend-requests/

You are given an integer n indicating the number of people in a network. Each person is labeled from 0 to n - 1.

You are also given a 0-indexed 2D integer array restrictions, where restrictions[i] = [xi, yi] means that person xi
and person yi cannot become friends, either directly or indirectly through other people.

Initially, no one is friends with each other. You are given a list of friend requests as a 0-indexed 2D integer array
requests, where requests[j] = [uj, vj] is a friend request between person uj and person vj.

A friend request is successful if uj and vj can be friends. Each friend request is processed in the given order (i.e.,
requests[j] occurs before requests[j + 1]), and upon a successful request, uj and vj become direct friends for all
future friend requests.

Return a boolean array result, where each result[j] is true if the jth friend request is successful or false if it is
not.

Note: If uj and vj are already direct friends, the request is still successful.

Example 1:

Input: n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]
Output: [true,false]
Explanation:
Request 0: Person 0 and person 2 can be friends, so they become direct friends.
Request 1: Person 2 and person 1 cannot be friends since person 0 and person 1 would be indirect friends (1--2--0).
'''

from collections import defaultdict, deque
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:

        def bfs(node):
            q = deque([node])
            visited = set()
            visited.add(node)
            relations = set()
            while q:
                node = q.popleft()
                relations.add(node)
                for neighbor in friend_mapping[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            return relations

        banned_mapping = defaultdict(set)
        for u, v in restrictions:
            banned_mapping[u].add(v)
            banned_mapping[v].add(u)

        result = [False] * len(requests)
        friend_mapping = defaultdict(set)
        for index, req in enumerate(requests):
            u, v = req[0], req[1]
            if v in banned_mapping[u]:
                result[index] = False
            else:
                set1 = bfs(u)
                set2 = bfs(v)
                banned = False
                for key in set1:
                    for bannedId in banned_mapping[key]:
                        if bannedId in set2:
                            result[index] = False
                            banned = True
                if not banned:
                    result[index] = True
                    friend_mapping[u].add(v)
                    friend_mapping[v].add(u)
        return result