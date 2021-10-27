'''Employee Importance - https://leetcode.com/problems/employee-importance/
You have a data structure of employee information, which includes the employee's unique ID,
their importance value, and their direct subordinates' IDs.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
Given an integer id that represents the ID of an employee, return the total importance value of this
employee and all their direct subordinates.

Example 1:

Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
'''
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        mapping = {}
        for employee in employees:
            mapping[employee.id] = [employee.importance, employee.subordinates]

        self.importance = 0

        def getImportanceValues(employee):
            subordinates = employee[1]
            self.importance += employee[0]
            for subordinate in subordinates:
                getImportanceValues(mapping[subordinate])

        getImportanceValues(mapping[id])
        return self.importance