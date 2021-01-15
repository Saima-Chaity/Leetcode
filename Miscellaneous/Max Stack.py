# Max Stack - https://leetcode.com/problems/max-stack/
'''Design a max stack data structure that supports the stack operations and supports finding the stack's
maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element,
only remove the top-most one.

Example 1:

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.'''

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxStack = []
        self.originalStack = []

    def push(self, x: int) -> None:
        self.originalStack.append(x)
        if not self.maxStack or x >= self.maxStack[-1]:
            self.maxStack.append(x)

    def pop(self) -> int:
        if self.maxStack[-1] == self.originalStack[-1]:
            self.maxStack.pop()
        return self.originalStack.pop()

    def top(self) -> int:
        return self.originalStack[-1]

    def peekMax(self) -> int:
        if self.maxStack:
            return self.maxStack[-1]

    def popMax(self) -> int:
        maxNum = self.maxStack[-1]
        temp =[]
        while self.originalStack and self.originalStack[-1] != maxNum:
            temp.append(self.originalStack.pop())
        self.pop()
        while temp:
            current = temp.pop()
            self.originalStack.append(current)
            if not self.maxStack or current >= self.maxStack[-1]:
                self.maxStack.append(current)
        return maxNum



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()