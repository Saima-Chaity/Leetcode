'''Design Browser History - https://leetcode.com/problems/design-browser-history/

You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history
number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you
will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x,
you will forward only x steps. Return the current url after forwarding in history at most steps.

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");      // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");    // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");     // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                  // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                  // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);               // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");    // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);               // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                  // You are in "linkedin.com", move back two steps to "facebook.com" then to
                                        "google.com". return "google.com"
browserHistory.back(7);                  // You are in "google.com", you can move back only one step to "leetcode.com".
                                        return "leetcode.com"'''



# Doubly linked list
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentNode = ListNode(homepage)

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        newNode.prev = self.currentNode
        self.currentNode.next = newNode
        self.currentNode = newNode

    def back(self, steps: int) -> str:
        while steps > 0 and self.currentNode:
            if self.currentNode.prev is None:
                return self.currentNode.value
            self.currentNode = self.currentNode.prev
            steps -= 1
        return self.currentNode.value

    def forward(self, steps: int) -> str:
        while steps > 0 and self.currentNode:
            if self.currentNode.next is None:
                return self.currentNode.value
            self.currentNode = self.currentNode.next
            steps -= 1
        return self.currentNode.value

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# Using stack
class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.index += 1
        if self.index == len(self.stack):
            self.stack.append(url)
        else:
            self.stack[self.index] = url
            self.stack = self.stack[:self.index + 1]

    def back(self, steps: int) -> str:
        if self.index < steps:
            self.index = 0
        else:
            self.index -= steps
        return self.stack[self.index]

    def forward(self, steps: int) -> str:
        if self.index + steps >= len(self.stack):
            self.index = len(self.stack) - 1
        else:
            self.index += steps
        return self.stack[self.index]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)