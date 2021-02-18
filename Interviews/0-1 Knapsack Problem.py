'''
0-1 Knapsack Problem
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the
knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum
value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an
item, either pick the complete item or don’t pick it (0-1 property).
'''

def knapSack(capacity, weight, value, n):

    if n == 0 or capacity == 0:
        return 0

    if weight[n-1] > capacity:
        return knapSack(capacity, weight, value, n-1)
    else:
        return max(value[n-1]+knapSack(capacity-weight[n-1], weight, value, n-1), knapSack(capacity, weight, value, n-1))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
