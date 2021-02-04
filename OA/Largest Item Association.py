'''Largest Item Association

In order to improve customer experience, Amazon has developed a system to provide recommendations to the customer
regarding the item they can purchase. Based on historical customer purchase information, an item association can be
defined as - If an item A is ordered by a customer, then item B is also likely to be ordered by the same customer
(e.g. Book 1 is frequently orderered with Book 2). All items that are linked together by an item association can be
considered to be in the same group. An item without any association to any other item can be considered to be in its
own item association group of size 1.

Given a list of item association relationships(i.e. group of items likely to be ordered together), write an algorithm
that outputs the largest item association group. If two groups have the same number of items then select the group
which contains the item that appears first in lexicographic order.

Input
The itput to the function/method consists of an argument - itemAssociation, a list containing paris of string
representing the items that are ordered together.

Output
Return a list of strings representing the largest association group sorted lexicographically.

Example
Input:
itemAssociation: [
[Item1, Item2],
[Item3, Item4],
[Item4, Item5]
]

Output:
[Item3, Item4, Item5]

Explanation:
There are two item association groups:
group1: [Item1, Item2]
group2: [Item3,Item4,Item5]
In the available associations, group2 has the largest association. So, the output is [Item3, Item4, Item5].
'''

from collections import defaultdict, deque
class Solution:
    def largestItemsAssociation(self, itemAssociation):

        def dfs(visited, groups, node):
            visited.add(node)
            current = []
            for neighbor in groups[node]:
                if neighbor not in visited:
                    nextValues = dfs(visited, groups, neighbor)
                    if len(nextValues) > len(current):
                        current = nextValues
            visited.remove(node)
            current.insert(0, node)
            return current

        groups = defaultdict(list)
        for items in itemAssociation:
            if items[0] == items[1]:
                continue
            groups[items[0]].append(items[1])
            groups[items[1]].append(items[0])

        output = []
        for node in groups:
            visited = set()
            result = dfs(visited, groups, node)
            if len(result) > len(output):
                output = result
        return output


itemAssociation = [
    ['Item1', 'Item2'],
    ['Item3', 'Item4'],
    ['Item4', 'Item5']
]

print(Solution.largestItemsAssociation((), itemAssociation)) #[Item3, Item4, Item5]

itemAssociation = [
    ["Item1", "Item2"],
    ["Item2", "Item8"],
    ["Item2", "Item10"],
    ["Item10", "Item12"],
    ["Item10", "Item4"],
    ["Item10", "Item3"],
    ["Item3", "Item4"],
    ["Item4", "Item5"]
]
print(Solution.largestItemsAssociation((), itemAssociation)) #[Item1, Item2, Item10, Item3, Item4, Item5]

