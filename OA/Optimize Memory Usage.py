'''
Give a computer with total K memory space, and an array of foreground tasks and background tasks
the computer needs to do. Write an algorithm to find a pair of tasks from each array to maximize
the memory usage. Notice the tasks could be done without origin order.

Input
The input to the function/method consists of three arguments :
foregroundTask, an array representing the memory usage of the foreground tasks,
backgroundTask, an array representing the memory usage of the background tasks,
K, the total memory space of the computer.

Output
Return a list of pairs of the task ids.

Examples 1
Input:
foregroundTasks = [1, 7, 2, 4, 5, 6]
backgroundTasks = [3, 1, 2]
K = 6

Output:
[(3, 2), (4, 1), (5,-1)]

Explaination:
Here we have 5 foreground tasks: task 0 uses 1 memeory. task 1 uses 7 memeory. task 2 uses 2 memeory..
And 5 background tasks: task 0 uses 3 memeory. task 1 uses 1 memeory. task 2 uses 2 memeory..
We need to find two tasks with total memory usage sum <= K.
Here we can return the foreground task 3 and background task 2, which total use 6 units of memory.
Or we can return the foreground task 4 and background task 1. Also use total 6 units of memory.
Or we can return the foreground task 5 only without any background task. Also use total 6 units of memory.
'''

class Solution:
    def optimalUtilization(self, foregroundTasks, backgroundTasks, k):
        """
        Using 2 pointers technique to run from left of a and from right of b
        Store pairs in a dictionary, keep track closest_to_target. Return dict[closest_to_target]
        T(n): O(m + n)
        """

        if not foregroundTasks or not backgroundTasks or not k:
            return []

        def checkIndividualArrays(tasks, isForegound):
            maxTaskLessThanTarget = float('-inf')
            for task in tasks:
                if task < k:
                    maxTaskLessThanTarget = max(maxTaskLessThanTarget, task)
            if maxTaskLessThanTarget != float('-inf') and maxTaskLessThanTarget in dict:
                if isForegound:
                    dict.get(maxTaskLessThanTarget).append((maxTaskLessThanTarget, -1))
                else:
                    dict.get(maxTaskLessThanTarget).append((-1, maxTaskLessThanTarget))
            return dict

        foregroundTasks.sort()
        backgroundTasks.sort()

        dict = {}
        closest_to_origin = 0
        minValue = float('inf')

        # 2 pointers:
        # - i run from left -> right of a
        # - j run from right -> left of b

        i = 0
        j = len(backgroundTasks) - 1

        while i < len(foregroundTasks) and j >= 0:
            sum = foregroundTasks[i] + backgroundTasks[j]
            if sum < k:
                if sum not in dict:
                    dict[sum] = [(foregroundTasks[i], backgroundTasks[j])]
                else:
                    dict.get(sum).append((foregroundTasks[i], backgroundTasks[j]))

                i += 1
                if k - sum < minValue:
                    minValue = k - sum
                    closest_to_origin = sum
            else:
                j -= 1

        checkIndividualArrays(foregroundTasks, True)
        checkIndividualArrays(backgroundTasks, False)
        return dict[closest_to_origin]


foregroundTasks = [1, 7, 2, 4, 5, 6]
backgroundTasks = [3, 1, 2]
K = 6

#Output: [(3, 2), (4, 1), (5,-1)]
print(Solution.optimalUtilization((), foregroundTasks, backgroundTasks, K))
