# Two Sum III - Data structure design - https://leetcode.com/problems/two-sum-iii-data-structure-design/
'''Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false'''

class TwoSum:

    def __init__(self):
        self.mapping = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.mapping:
            self.mapping[number] = 1
        else:
            self.mapping[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.mapping.keys():
            remaining = value - num
            if remaining != num:
                if remaining in self.mapping:
                    return True
            elif self.mapping[num] > 1:
                return True
        return False

# TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)