# Split Linked List in Parts - https://leetcode.com/problems/split-linked-list-in-parts/
'''Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive
linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1.
This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have
a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:

        length = 0
        current = root
        output = []
        while current:
            current = current.next
            length += 1

        itemCount = length // k
        extraItem = length % k
        current = root
        prev = None
        while current:
            if current:
                output.append(current)
                itemLength = itemCount + 1 if extraItem > 0 else itemCount
                extraItem -= 1
                for i in range(itemLength):
                    prev = current
                    current = current.next
                prev.next = None
            else:
                output.append(None)

        while len(output) < k:
            if not current:
                output.append(None)
        return output


