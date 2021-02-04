'''Count LRU Cache Misses
A virtual memory management system use least-recently-Used (LRU) cache. When a requested memory page
is not in the cache and the cache is full, the page that was least-recently-used should be removed
from the cache to make room for the requested page. If the cache is not full, the requested page can
simply be added to the cache and considered the most-recently-used page in the cache. A given page
should occur at most once in the cache.

Given the maximum size of the cache and a list of page requests,write an algorithm to calculate the
number of cache misses. A cache miss occurs when a page is requested and isn't found in the cache.

int lruCacheMisses(int num, List<Integer> pages, int maxCacheSize)
Input
The input consists of three arguments:

num : an integer representing the number of pages

pages : a list of integers representing the pages requested

maxCacheSize : an integer representing the size of the cache

Output
Return an integer for the number of cache misses.

Note
The cache is initially empty and the list contains pages numbered in the range 1-50. A page at
index "i" in the list is requested before a page at index "i+1".

Constraints
0 <= i < num

Examples
Example 1:
Input:
num = 6

pages = [1,2,1,3,1,2]

maxCacheSize = 2

Output: 4
Explanation: Cache state as requests come in ordered longest-time-in-cache to shortest-time-in-cache:

1*

1,2*

2,1

1,3*

3,1

1,2*

Asterisk (*) represents a cache miss. Hence, the total number of a cache miss is `4`.'''


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

class Solution:
    def LRUCacheMisses(self, num, pages, maxCacheSize):

        cache = LRUCache(maxCacheSize)
        misses = 0
        for page in pages:
            if cache.get(page) == -1:
                misses += 1
            cache.put(page, None)
        return misses

num = 6
pages = [1,2,1,3,1,2]
maxCacheSize = 2
print(Solution.LRUCacheMisses((), num, pages, maxCacheSize))