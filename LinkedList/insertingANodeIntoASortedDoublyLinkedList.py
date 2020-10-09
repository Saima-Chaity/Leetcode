# Inserting a Node Into a Sorted Doubly Linked List

# Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  
# and insert it at the proper location to maintain the sort.

class DoublyLinkedListNode:
    def __init__(self, data=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def sortedInsert(head, data):
        current = head
        newNode = DoublyLinkedListNode(data)

        # If the node is to be inserted at   
        # the beginning of the doubly linked list  
        if head.data >= newNode.data:
            newNode.next = head
            newNode.next.prev = newNode
            head = newNode
        else:
            current = head
            # Locate the node after which  
            # the new node  is to be inserted 
            while current.next and current.next.data < newNode.data:
                current = current.next
            
            # Make the appropriate links 
            newNode.next = current.next

            # If the new node is not inserted  
            # at the end of the list 
            if current.next:
                newNode.next.prev = newNode
            newNode.prev = current
            current.next = newNode
        return head