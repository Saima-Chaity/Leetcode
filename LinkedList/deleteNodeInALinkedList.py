# Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/
'''Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next is not None:
            node.val = node.next.val
            node.next = node.next.next



'''Given a Singly Linked List, write a function to delete a given node. Your function must follow following constraints:
1) It must accept a pointer to the start node as the first parameter and node to be deleted as the second parameter i.e., a pointer to head node is not global.
2) It should not return a pointer to the head node.
3) It should not accept pointer to pointer to the head node.

You may assume that the Linked List never becomes empty.'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        temp = head
        prev = head

        if temp.val == node:
            if not temp.next:
                print("Can't delete last node")
            else:
                temp.val = temp.next.val
                temp.next = temp.next.next
        
        while temp.next and temp.val != node:
            prev = temp
            temp = temp.next
        
        if not temp.next and temp.val != node:
            print("Can't delete last node")
        
        if not temp.next and temp.val == node:
            prev.next = None
        else:
            prev.next = temp.next
        
        
