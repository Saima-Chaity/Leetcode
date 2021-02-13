# Accounts Merge - https://leetcode.com/problems/accounts-merge/
'''Given a list accounts, each element accounts[i] is a list of strings, where the first
element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some
email that is common to both accounts. Note that even if two accounts have the same name, they may belong to
different people as people could have the same name. A person can have any number of accounts initially, but
all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is
the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
 ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'],
['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.'''

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph = defaultdict(set)
        emailToName = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                emailToName[email] = name

        visited = set()
        output = []
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                components = []
                while stack:
                    node = stack.pop()
                    components.append(node)
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            stack.append(neighbour)
                output.append([emailToName[email]] + sorted(components))
        return output


# Union - find
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def find(node):
            if parent[node] < 0:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            a, b = find(a), find(b)
            if a != b:
                if parent[a] < parent[b]:
                    parent[a] += parent[b]
                    parent[a] = b
                else:
                    parent[b] += parent[a]
                    parent[b] = a

        index, parent, email_to_id, id_to_name = 0, [], {}, {}
        for account in accounts:
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = index
                    id_to_name[index] = account[0]
                    parent.append(-1)
                    index += 1
                union(email_to_id[account[1]], email_to_id[email])

        res = {}
        for email, id in email_to_id.items():
            master = find(id)
            res[master] = res.get(master, []) + [email]
        return [[id_to_name[id]] + sorted(emails) for id, emails in res.items()]