# Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/
'''Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false'''

# Using two queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.topElement = -1

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        self.topElement = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) > 1:
            self.topElement = self.queue1.pop(0)
            self.queue2.append(self.topElement)
        removedItem = self.queue1.pop()
        self.queue1 = self.queue2
        self.queue2 = []
        return removedItem

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.topElement

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Using one queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        qLength = len(self.queue1)
        while qLength > 1:
            self.queue1.append(self.queue1.pop(0))
            qLength -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0


# Using doubly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        newNode = Node(x)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            newNode.prev = None
            self.head = newNode
        return self.head

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.head:
            return None
        if not self.head.next:
            temp = self.head.value
            self.head = None
            return temp
        else:
            temp = self.head.value
            self.head = self.head.next
            self.head.prev = None
            return temp

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.head:
            return self.head.value

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.head:
            return False
        return True
