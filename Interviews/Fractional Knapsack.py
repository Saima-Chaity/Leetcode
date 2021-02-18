'''Fractional Knapsack

Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum
total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item.
'''

import heapq
def getMaxValue(weight, value, capacity):

    valueByWeight = []
    for i in range(len(value)):
        heapq.heappush(valueByWeight, (-(value[i]//weight[i]), value[i], weight[i]))

    totalValue = 0
    while valueByWeight:
        ratio, currentValue, currentWeight = heapq.heappop(valueByWeight)
        if capacity - currentWeight >= 0:
            capacity -= currentWeight
            totalValue += currentValue
        else:
            fraction = capacity / currentWeight
            totalValue += currentValue * fraction
            capacity = int(capacity - (currentWeight * fraction))
            break
    return totalValue

if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50

    # Function call
    maxValue = getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)