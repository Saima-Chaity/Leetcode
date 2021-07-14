'''
Min Steps to Make Piles Equal Height

Alexa is given n piles of equal or unequal heights. In one step, Alexa can remove any number of boxes from the
pile which has the maximum height and try to make it equal to the one which is just lower than the maximum height
of the stack. Determine the minimum number of steps required to make all of the piles equal in height.

Example 1:

Input: piles = [5, 2, 1]
Output: 3
Explanation:
Step 1: reducing 5 -> 2 [2, 2, 1]
Step 2: reducing 2 -> 1 [2, 1, 1]
Step 3: reducing 2 -> 1 [1, 1, 1]
So final number of steps required is 3.
'''

''' Time  : O(N log N)
    Space : O(1), where N = len(s)
'''
def min_steps_balance(piles):

    if len(piles) < 2:
        return 0

    piles = sorted(piles, reverse=True)
    minStepsRequired = 0
    for i in range(1, len(piles)):
        if piles[i] != piles[i-1]:
            minStepsRequired += i
    return minStepsRequired

if __name__ == "__main__":
    print(min_steps_balance([50]) == 0)
    print(min_steps_balance([10, 10]) == 0)
    print(min_steps_balance([5, 2, 1]) == 3)
    print(min_steps_balance([4, 2, 1]) == 3)
    print(min_steps_balance([4, 5, 5, 4, 2]) == 6)
    print(min_steps_balance([4, 8, 16, 32]) == 6)
    print(min_steps_balance([4, 8, 8]) == 2)
    print(min_steps_balance([4, 4, 8, 8]) == 2)
    print(min_steps_balance([1, 2, 2, 3, 3, 4]) == 9)
    print(min_steps_balance([1, 1, 2, 2, 2, 3, 3, 3, 4, 4]) == 15)


