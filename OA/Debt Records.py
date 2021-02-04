'''Debt Records
The Company is working on a new application for recording internal debts across teams. This program
can be used to create groups that show all records of debts between the group members. Given the
group debt records observed for this team (including the borrower name, lender name, and debt amount),
who in the group has the smallest negative balance?

Notes: -10 is smaller than -1. If multiple people have the smallest negative balance, return the
list in alphabetical order. If nobody has a negative balance, return the list consisting of the
string "Nobody has a negative balance".

Write an algorithm to find who in the group has the smallest negative balance.

Input
The input consists of three arguments:

numCols: an integer representing the number of elements in debt records. It is always 3

numRows : an integer representing the number of debt records

debts: a list of triplets representing debtRecord consisting of a string borrower, a string lender,
and an integer amount, representing the debt record.

Output
Return a list of strings representing an alphabetically ordered list of members with the smallest
negative balance. If no team member has a negative balance then return a list containing the string
"Nobody has a negative balance".

Constraints
1 ≤ numRows ≤ 2*10^5

1 ≤ amount in debts ≤ 1000

1 ≤ length of borrower and lender in debts ≤ 20

Example
Borrower	Lender	amount
Alex	Blake	2
Blake	Alex	2
Casey	Alex	5
Blake	Casey	7
Alex	Blake	4
Alex	Casey	4
Explanation:
For Alex:
The first, fifth, and sixth entries decrease the balance because he is a borrower.

The second and third entries increase because he is a lender.

His balance is (2 + 5) - (2 + 4 + 4) = 7 - 10 = -3.

For Blake:
He is lender in first and fifth entries and a borrower in the second and fourth entries.

His balance is (2 + 4) - (2 + 7) = 6 - 9 = -3.

For Casey:
He is a borrower in the third entry and a lender in the fourth and sixth entries.

Thus, Casey's balance is (7 + 4) - 5 = 11 - 6 = 5.

Here Alex and Blake both have the balance of -3, which is the minimum amoung all members.
'''

class Solution:
    def debtRecord(self, numCols, numRows, debtRecords):
        if not debtRecords:
            return "Nobody has a negative balance"

        mapping = {}
        for record in debtRecords:
            borrower = record[0]
            lender = record[1]
            amount = record[2]
            mapping[borrower] = mapping.get(borrower, 0) - amount
            mapping[lender] = mapping.get(lender, 0) + amount

        output = []
        for person, amount in mapping.items():
            if amount < 0:
                output.append(person)

        if not output:
            return "Nobody has a negative balance"

        if len(output) > 1:
            output.sort()
        return output


numCols = 3
numRows = 6
debtRecords = [['Alex', 'Blake', 2], ['Blake', 'Alex', 2], ['Casey', 'Alex', 5],
               ['Blake', 'Casey', 7], ['Alex', 'Blake', 4], ['Alex', 'Casey', 4]]
print(Solution.debtRecord((),numCols, numRows, debtRecords))