# Number of Equivalent Domino Pairs - https://leetcode.com/problems/number-of-equivalent-domino-pairs/

'''Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if
either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1'''


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        output = 0
        map = {}
        for domino in dominoes:
            domino = tuple(sorted(domino))
            if domino not in map:
                map[domino] = 1
            else:
                map[domino] += 1

        for count in map.values():
            pair = count * (count - 1) // 2
            output += pair
        return output