'''Turnstile

A small store having exactly one turnstile. It can be used by customers either as an entrance or an exit.
Sometimes multiple customers want to pass through the turnstile and their directions can be different.
The ith customer comes to the turnstile at time[i] and wants to either exit the store if direction[i] = 1 or
enter the store if direction[i] = 0. Customers form 2 queues, one to exit and one to enter. They are ordered
by the time when they came to the turnstile and, if the times are equal, by their indices.

If one customer wants to enter the store and another customer wants to exit at the same moment, there are three cases:

If in the previous second the turnstile was not used (maybe it was used before, but not at the previous second),
then the customer who wants to exit goes first.
If in the previous second the turnstile was used as an exit, then the customer who wants to leave goes first.
If in the previous second the turnstile was used as an entrance, then the customer who wants to enter goes first.
Passing through the turnstile takes 1 second.

Write an algorithm to find the time for each customer when they will pass through the turnstile.

Input
The input consists of three arguments:

numCustomers : an integer representing the number of customers (n)

arrTime: a list of integers where the value at index i is the time in seconds when the ith customer will come
to the turnstile

direction: a list of integers where the value at index i is the direction of the ith customer

Output
Return a list of integers where the value at index i is the time when the ith customer will pass the turnstile.

Constraints
1 <= numCustomers <= 10^5

0 <= arrTime[i] <= arrTime[i + 1] <= 10^9

0 <= i <= numCustomers - 2

0 <= direction[i] <= 1

0 <= j <= numCustomers - 1

Examples
Example 1:
Input:
numCustomers = 4

arrTime = [0, 0, 1,5]

direction = [0, 1, 1, 0]

Output: [2,0,1,5]
Explanation:
At time 0, customer 0 and 1 want to pass through the turnstile. Customer 0 wants to enter the store and customer 1 wants
to exit the store. The turnstile was not used in the previous second, so the priority is on the side of the customer 1
At time 1, customers 0 and 2 want to pass through the turnstile. Customer 2 wants to exit the store and at the previous
second the turnstile was used as an exit, so the customer `2 passes through the turnstile.
At time 2, customer 0 passes through the turnstile.
At time 5, customer 3 passes through the turnstile.
Example 2:
Input:
numCustomers = 5

arrTime = [0,1,1,3,3]

direction = [0, 1, 0, 0, 1]

Output: [0, 2, 1, 4, 3]
Explanation:
At time 0, customer 0 passes through the turnstile (enters).
At time 1, customers 1 (exit) and 2 (enter) want to pass through the turnstile, and customer 2 passes through the
turnstile because their direction is equal to the direction at the previous second.
At time 2. customer 1 passes through the turnstile (exit).
At time 3, customers 3 (enter) and 4 (exit) want to pass through the turnstile. Customer 4 passes through the turnstile
because at the previous second the turnstile was used to exit.
At time 4, customer 3 passes through the turnstile.
'''

class Solution:
    def turnstile(self, numCustomers, time, direction):
        enter = []
        exit = []
        result = [0] * numCustomers
        for i in range(len(time)):
            if direction[i] == 1:
                exit.append([time[i], i])
            elif direction[i] == 0:
                enter.append([time[i], i])

        lastUsed = -1
        timeCounter = 0
        while enter or exit:
            # Process the exit queue if and only if following conditions are satisfied
            # If exit queue is not empty and the person at the front of the queue can go out based on his time stamp
            # and ( Nothing happened at last time stamp i.e. nobody moved in or out so lastTurn will be -1 in this case
            # or, somebody moved out at last time stamp, in this case lastTurn will be 1
            # or, nobody is there in the entrance queue
            # or, at last time stamp somebody got in but the person at the front of the queue can't go in due to their
            # timestamp
            if exit and exit[0][0] <= timeCounter and (lastUsed == -1 or lastUsed == 1 or not enter or \
                                                       (lastUsed == 0 and enter[0][0] > timeCounter)):
                result[exit[0][1]] = timeCounter
                lastUsed = 1
                exit.pop(0)
            elif enter and enter[0][0] <= timeCounter:
                result[enter[0][1]] = timeCounter
                lastUsed = 0
                enter.pop(0)
            else:
                lastUsed = -1
            timeCounter += 1
        return result

numCustomers = 4
arrTime = [0, 0, 1,5]
direction = [0, 1, 1, 0]
print(Solution.turnstile((), numCustomers, arrTime, direction)) # Output: [2,0,1,5]


numCustomers = 5
arrTime = [0,1,1,3,3]
direction = [0, 1, 0, 0, 1]
print(Solution.turnstile((), numCustomers, arrTime, direction)) # Output: [0, 2, 1, 4, 3]