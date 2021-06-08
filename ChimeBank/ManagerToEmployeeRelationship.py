'''you are given a string
"1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2"

the format of the string is "id:name:manager_id"

Print this:

Ann
- Alb
- edomnd
-- max

for string "1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2, 5: bruce:0" it would print

Bruce
Ann
- Alb
- edomnd
-- max

or

Ann
- Alb
- edomnd
-- max
Bruce
'''

from collections import defaultdict
class Solution:
    def getHeirarcy(inputStr):
        managerToEmp = defaultdict(list)
        empNames = {}
        for item in inputStr.split(","):
            emp_id, emp_name, managerId = item.split(':')
            managerToEmp[int(managerId)].append(int(emp_id))
            empNames[int(emp_id)] = emp_name

        def printHeirarchy(id, level):
            if id != 0:
                print("-" * level + empNames[id])

            for reportee in managerToEmp[id]:
                printHeirarchy(reportee, level+1 if id != 0 else level)

        return printHeirarchy(0, 0)


# Solution.getHeirarcy('1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2, 5:bruce:0')
# print("=====")
# Solution.getHeirarcy('1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2')



from collections import defaultdict
class Solution1:

    def __init__(self, input):
        self.input = input

    def org(self):
        self.managers = defaultdict(list)
        self.employee = {}
        for item in self.input.split(","):
            empId, name, managerId = item.split(":")
            self.managers[int(managerId)].append(int(empId))
            self.employee[int(empId)] = name
        self.printOrg(0, 0)

    def printOrg(self, id, level):

        if id != 0:
            print("-" * level + " " + self.employee[id])

        for reportee in self.managers[id]:
            self.printOrg(reportee, level + 1 if id != 0 else level)

c = Solution1('1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2')
c.org()

# Solution1.org((), '1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2, 5:bruce:0')
# print("=====")
# Solution1.org((), '1:max:4, 2:ann:0, 3:alb:2, 4:edmond:2')