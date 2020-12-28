# Exclusive Time of Functions - https://leetcode.com/problems/exclusive-time-of-functions/
'''On a single-threaded CPU, we execute a program containing n functions. Each function
has a unique ID between 0 and n-1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed
onto the stack, and when a function call ends, its ID is popped off the stack. The function
whose ID is at the top of the stack is the current function being executed. Each time a function
starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents the ith log message formatted as a string
"{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call
with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call
with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple
times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program.
For example, if a function is called twice, one call executing for 2 time units and another call
executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array, where the value at the ith index represents
the exclusive time for the function with ID i.'''


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        result = [0] * n
        stack = []
        for log in logs:
            splitedLog = log.split(":")
            logId = int(splitedLog[0])
            message = splitedLog[1]
            timeStamp = int(splitedLog[2])
            if message == "start":
                stack.append((logId, timeStamp))
            else:
                totalTime = (timeStamp - int(stack[-1][1])) + 1
                stack.pop()
                result[logId] += totalTime
                if stack:
                    result[stack[-1][
                        0]] -= totalTime  # if stack is not empty means current stack still has a process running,
                                          # and that process need to reduce the other process running time
        return result

