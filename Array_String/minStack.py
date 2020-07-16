# Min Stack - https://leetcode.com/problems/min-stack/
'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2'''

class MinStack:

    def __init__(self):
        """
        initialize data structure here.
        """
        self.minStack = []
        self.originalStack = []

    def push(self, x: int) -> None:
        self.originalStack.append(x)
        if len(self.minStack) == 0:
            self.minStack.append(x)
        elif x <= self.minStack[-1]:
            self.minStack.append(x)
        return self.originalStack

    def pop(self) -> None:
        if self.minStack[-1] == self.originalStack[-1]:
            self.minStack.pop()
        return self.originalStack.pop()

    def top(self) -> int:
        return self.originalStack[-1]

    def getMin(self) -> int:
        if len(self.minStack) != 0:
            return self.minStack[-1]


# MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()