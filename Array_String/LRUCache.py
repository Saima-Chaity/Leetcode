# LRU Cache - https://leetcode.com/problems/lru-cache/
'''Design and implement a data structure for Least Recently Used (LRU) cache. It should support
the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache
reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4'''

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key, last=False)
            return self.dict[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        self.dict[key] = value
        self.dict.move_to_end(key, last=False)
        if len(self.dict) > self.capacity:
            self.dict.popitem()

# LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Using doubly linked list and hash map
class ListNode:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNewNode(self, node):
        # Add node right before the tail
        prevNode = self.tail.prev
        prevNode.next = node
        self.tail.prev = node
        
        node.prev = prevNode
        node.next = self.tail
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.removeNode(node)
            self.addNewNode(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.removeNode(self.dict[key])

        newNode = ListNode(key, value)
        self.dict[key] = newNode
        self.addNewNode(newNode)
        
        if len(self.dict) > self.capacity:
            # Remove head.next node because it is the least recently visited node
            node = self.head.next
            self.removeNode(node)
            del self.dict[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)