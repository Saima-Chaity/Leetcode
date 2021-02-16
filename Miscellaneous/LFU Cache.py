# LFU Cache - https://leetcode.com/problems/lfu-cache/
'''Design and implement a data structure for Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Sets or inserts the value if the key is not already present. When the cache reaches
its capacity, it should invalidate the least frequently used item before inserting a new item. For this problem,
when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be evicted.
Notice that the number of times an item is used is the number of calls to the get and put functions for that item
since it was inserted. This number is set to zero when the item is removed.

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]'''

from collections import defaultdict
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return self.size

    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return
        if not node:
            node = self.tail.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.frequency = defaultdict(DLinkedList)
        self.minfreq = 0 # frequency of the last linked list (the minimum frequency of entire LFU cache)
        self.capacity = capacity
        self.size = 0

    def update(self, node):
        freq = node.freq
        self.frequency[freq].pop(node)

        #if current list the last list which has lowest frequency and current node is the only node in that list
        #we need to remove the entire list and then increase min frequency value by 1
        if self.minfreq == freq and not self.frequency[freq]:
            self.minfreq += 1
        node.freq += 1
        freq = node.freq
        self.frequency[freq].append(node)

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.update(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.dict:
            node = self.dict[key]
            self.update(node)
            node.value = value
        else:
            if self.size == self.capacity:
                node = self.frequency[self.minfreq].pop()
                del self.dict[node.key]
                self.size -= 1

            node = ListNode(key, value)
            self.dict[key] = node
            self.frequency[1].append(node)
            self.minfreq = 1
            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)