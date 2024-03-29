# Reorder Data in Log Files - https://leetcode.com/problems/reorder-data-in-log-files/
'''You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that
each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs
are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 '''


'''Time: O(MKlogK), with k = len(letter_logs) M = length of a single log
Space: MN'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digitLogs = []
        letterLogs = []
        for log in logs:
            identifiers, metadata = log.split(" ", 1)
            if metadata[0].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append([log, metadata, identifiers])

        letterLogs.sort(key=lambda x: (x[1], x[2]))
        result = [log[0] for log in letterLogs] + digitLogs
        return result
