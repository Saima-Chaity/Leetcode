'''A node can be added in three ways:
1) At the front of the linked list
2) At a specific position.
3) At the end of the linked list.'''

# Insert At the front of the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtTheFront(self, head: ListNode, data) -> ListNode:
        nodeToBeInserted = ListNode(data)
        nodeToBeInserted.next = head
        head = nodeToBeInserted
        return head


# Insert At a specific position of the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtSpecificPosition(self, head: ListNode, data, position) -> ListNode:
        nodeToBeInserted = ListNode(data)
        currentPosition = 0
        prev = None
        current = head
        while current and currentPosition < position:
            currentPosition += 1
            prev = current
            current = current.next
        nextNode = current
        prev.next = nodeToBeInserted
        nodeToBeInserted.next = nextNode
        return head


# Insert At the end of the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtTheEnd(self, head: ListNode, data) -> ListNode:
        nodeToBeInserted = ListNode(data)
        if not head:
            head = nodeToBeInserted
            return head

        lastNode = head
        while lastNode:
            lastNode = lastNode.next
        lastNode.next = nodeToBeInserted
        return head