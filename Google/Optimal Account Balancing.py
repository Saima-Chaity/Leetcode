'''Optimal Account Balancing - https://leetcode.com/problems/optimal-account-balancing/

You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that
the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.

Example 1:

Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:

Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #0 only need to give person #1 $4, and all debt is settled.'''

'''We use index i for positives and index j for negatives. For each positive[i], 
we try all the combinations of j that pay up positive[i], and then move to next i.'''

from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        def dfs(positives, negatives, positives_index, negatives_index):
            if positives_index == len(positives):
                return 0
            if positives[positives_index] == 0:
                return dfs(positives, negatives, positives_index + 1, 0)
            min_step = float('inf')
            for j in range(negatives_index, len(negatives)):
                if negatives[j] == 0:
                    continue
                due_amount = min(-negatives[j], positives[positives_index])
                positives[positives_index] -= due_amount
                negatives[j] += due_amount
                min_step = min(min_step, 1 + dfs(positives, negatives, positives_index, j + 1))
                positives[positives_index] += due_amount
                negatives[j] -= due_amount
            return min_step

        balances = defaultdict(int)
        for from_person, to_person, amount in transactions:
            balances[from_person] += amount
            balances[to_person] -= amount

        # Negative needs to pay back to the positive
        positives = []
        negatives = []
        for key, value in balances.items():
            if value > 0:
                positives.append(value)
            else:
                negatives.append(value)

        return dfs(positives, negatives, 0, 0)
