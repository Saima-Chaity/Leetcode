'''First Unique Number - https://leetcode.com/problems/first-unique-number/

You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if
there is no such integer.
void add(int value) insert value to the queue.

Example 1:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]
Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
'''

from collections import deque
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.isUnique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.q and not self.isUnique[self.q[0]]:
            self.q.popleft()

        if self.q:
            return self.q[0]
        return -1

    def add(self, value: int) -> None:
        if value not in self.isUnique:
            self.isUnique[value] = True
            self.q.append(value)
        else:
            self.isUnique[value] = False

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)