# Analyze User Website Visit Pattern - https://leetcode.com/problems/analyze-user-website-visit-pattern/
'''We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.
(The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution,
return the lexicographically smallest such 3-sequence.

Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
timestamp = [1,2,3,4,5,6,7,8,9,10],
website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation:
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.'''

from collections import defaultdict
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        tuples = zip(timestamp, username, website)
        sorted_tuples = sorted(tuples)

        mapping = defaultdict(list)
        for timestamp, user, website in sorted_tuples:
            mapping[user].append(website)

        counterDict = defaultdict(int)
        for website in mapping.values():
            combination = set(combinations(website, 3))
            for item in combination:
                counterDict[item] += 1

        sortedOutput = sorted(counterDict, key=lambda x: (-counterDict[x], x))  # sort descending by value,
                                                                                # then lexicographically
        return sortedOutput[0]