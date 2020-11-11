'''Compare two strings represented as linked lists
Given two strings, represented as linked lists (every character is a node in a linked list). Write a function compare() 
that works similar to strcmp(), i.e., it returns 0 if both strings are same, 1 if first linked list is lexicographically 
greater, and -1 if the second string is lexicographically greater.

Examples:

Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s->b
Output: -1
'''

class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.char = key 
        self.next = None

class Solution:
    def compareStr(list1, list2):
        while list1 and list2 and list1.char == list2.char:
            list1 = list1.next 
            list2 = list2.next 
        
        if list1 and list2:
            return 1 if list1.char > list2.char else -1
        
        if list2 and not list1:
            return -1
        if list1 and not list2:
            return 1
        return 0