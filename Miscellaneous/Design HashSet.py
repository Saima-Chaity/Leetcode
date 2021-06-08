'''Design HashSet - https://leetcode.com/problems/design-hashset/

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
'''


'''Linked List'''
class LinkedList:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.bucket = [None] * self.size

    def add(self, key: int) -> None:
        index = key % self.size
        if self.bucket[index] == None:
            self.bucket[index] = LinkedList(key)
        else:
            current = self.bucket[index]
            while True:
                if current.key == key:
                    return None
                if current.next == None:
                    break
                current = current.next
            current.next = LinkedList(key)

    def remove(self, key: int) -> None:

        index = key % self.size
        if self.bucket[index] != None:
            current = self.bucket[index]
            if current.key == key:
                self.bucket[index] = current.next
            else:
                while current.next:
                    if current.next.key == key:
                        current.next = current.next.next
                        break
                    current = current.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size
        if self.bucket[index] == None:
            return False
        else:
            current = self.bucket[index]
            while True:
                if current.key == key:
                    return True
                if current.next == None:
                    break
                current = current.next

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


'''BST'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insertIntoBST(self, root, value):
        if not root:
            return TreeNode(value)
        if root.value == value:
            return root
        elif value > root.value:
            root.right = self.insertIntoBST(root.right, value)
        else:
            root.left = self.insertIntoBST(root.left, value)
        return root

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.value

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.value

    def deleteNode(self, root, key):
        if not root:
            return None
        if key > root.value:
            root.right = self.deleteNode(root.right, key)
        elif key < root.value:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.value = self.successor(root)
                root.right = self.deleteNode(root.right, root.value)
            else:
                root.value = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.value)
        return root

    def search(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self.search(root.left, value)
        return self.search(root.right, value)


class Bucket:
    def __init__(self):
        self.tree = BST()

    def insert(self, value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)

    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)

    def exists(self, value):
        return (self.tree.search(self.tree.root, value) is not None)


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.bucket = [Bucket()] * self.size

    def hashIndex(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self.hashIndex(key)
        self.bucket[index].insert(key)

    def remove(self, key: int) -> None:
        index = self.hashIndex(key)
        self.bucket[index].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = self.hashIndex(key)
        return self.bucket[index].exists(key)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)