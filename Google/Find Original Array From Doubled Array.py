'''Find Original Array From Doubled Array - https://leetcode.com/problems/find-original-array-from-doubled-array/

An integer array original is transformed into a doubled array changed by appending twice the value of
every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array,
return an empty array. The elements in original may be returned in any order.

Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
'''

from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if len(changed) % 2 != 0:
            return []

        mapping = defaultdict(int)
        for num in changed:
            mapping[num] += 1

        if mapping[0] % 2 == 1:
            return []

        changed.sort()
        result = []
        for i in range(len(changed)):
            if mapping[changed[i]] > mapping[changed[i] * 2]:
                return []

            if mapping[changed[i]] and mapping[changed[i] * 2]:
                result.append(changed[i])
                mapping[changed[i]] -= 1
                mapping[changed[i] * 2] -= 1

            if len(result) == len(changed) // 2:
                return result

        return []
