# Insert into a Sorted Circular Linked List - https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
'''Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value
insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single
node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the
insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference
to that single node. Otherwise, you should return the original given node.

Example 1:

Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to
the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3.
After the insertion, the list should look like this, and we should still return node 3.'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal)
            head = newNode
            newNode.next = head
            return head

        newNode = Node(insertVal)
        prev = head
        current = head.next

        while True:
            if prev.val <= newNode.val <= current.val:
                break
            elif prev.val > current.val:  # The value of new node goes beyond the minimal and
                                          # maximal values of the current list.
                if prev.val <= newNode.val and newNode.val >= current.val:
                    break
                elif prev.val >= newNode.val and newNode.val <= current.val:
                    break

            prev = current
            current = current.next

            if prev == head:
                break

        prev.next = newNode
        newNode.next = current
        return head
