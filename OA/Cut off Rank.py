''' Cut off Rank
A group of work friends playing a competitive video game together. During the game, each player
receives a certain amount of points based on their performance. At the end of a round, players who
achieve at least a cutoff rank get to "level up" their character, gaining increased abilities for
them. Given the scores of the players at the end of the round, how many players will be able to
level up their character?

Note that players with equal scores will have equal ranks, but the player with the next lowest
score will be ranked based on the position within the list of all players' scores. For example,
if there are four players, and three players tie for first place, their ranks would be 1,1,1,
and 4. Also, no player with a score of O can level up, no matter what their rank.

Write an algorithm that returns the count of players able to level up their character.

Input
The input consists of three arguments:

cutOffRank: an integer representing the number of elements in debt records. It is always 3

num : an integer representing the number of debt records

scores: a list of triplets representing debtRecord consisting of a string borrower, a string
lender, and an integer amount, representing the debt record.

Output
Return an integer representing the number of players who will be able to level up their
characters at the end of the round.

Constraints:
1 <= num <= 10^5
0 <= scores[i] <= 100
0 <= i < num
cutOffRank <= num
Examples
Example 1:
Input: cutOffRank = 3, num = 4, scores=[100, 50, 50, 25 ]
Output: 3
Explanation:
In order, the players achieve the ranks [4,4,3,2,1]. Since the cutOffRank is 4, all 5 players will be
able to level up their characters.

So, the output is 5.
'''

class Solution:
    def cutOffRank(self, cutOffRank, num, scores):
        scores.sort()
        prevScore = float('inf')
        total = 0
        for i in range(len(scores)-1, -1, -1):
            currentScore = scores[i]
            if currentScore == prevScore:
                total += 1
            else:
                if total >= cutOffRank:
                    break
                total += 1
                prevScore = currentScore
        return total


cutOffRank = 3
num = 4
scores = [100, 50, 50, 25]
print(Solution.cutOffRank((), cutOffRank, num, scores)) # 3

cutOffRank = 4
num = 5
scores = [2, 2, 3, 4, 5]
print(Solution.cutOffRank((), cutOffRank, num, scores)) # 5