'''Min Adj Swaps to Group Red Balls

There are N balls positioned in a row. Each of them is either red or white . In one move we can swap two adjacent balls.
We want to arrange all the red balls into a consistent segment. What is the minimum number of swaps needed?

Given string S of length N built from characters "R" and "W", representing red and white balls respectively, returns
the minimum number of swaps needed to arrange all the red balls into a consistent segment.
If the result exceeds 10^9, return -1.

Example 1:
Input:WRRWWR
Output: 2
Explanation:
We can move the last ball two positions to the left:

swap R and W -> WRRWRW
swap R and W -> WRRRWW
Example 2:
Input:WWRWWWRWR
Output: 4
Explanation:
We can move the last ball two positions to the left:

swap R and W -> WWRWWWRRW
swap R and W -> WWWRWWRRW
swap R and W -> WWWWRWRRW
swap R and W -> WWWWWRRRW'''


def min_swaps(s: str) -> int:
    red_count = 0
    for char in s:
        if char == "R":
            red_count += 1

    start = 0
    end = len(s) - 1
    swapCount = 0

    while start < end:
        if s[start] == "R" and s[end] == "R":
            red_count -= 2
            swapCount += end - start - 1 - red_count
            start += 1
            end -= 1
        elif s[start] != "R":
            start += 1
        else:
            end -= 1

    return -1 if swapCount > 10 ** 9 else swapCount

print(min_swaps("WWRWWWRWR"))