# Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/
'''Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, 
find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"
'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters)-1
        asciiValueOfTarget = ord(target)
        
        if asciiValueOfTarget >= ord(letters[len(letters)-1]):
            return letters[0]
        
        while low < high:
            mid = low + (high-low) // 2
            if ord(letters[mid]) <= asciiValueOfTarget:
                low = mid + 1
            else:
                high = mid
        return letters[low]