'''storage optimization
A company is experimenting with a flexible storage system for their warehouses. The storage unit
consists of a shelving system which is one meter deep with removable vertical and horizon separators.
When all separators are installed, each storage space is one cubic meter (1' x 1' x 1'). Determine the
volume of the largest space when series of horizontal and vertical separators are removed.

Example 1:
n = 6 m = 6 h = [4] v = [2] Consider the diagram below. The left image depicts the initial storage
unit with n = 6 horizon and m = 6 Vertical separators, where the volume of the largest storage space
is 1 x 1 x 1. The right image depicts that unit after the fourth horizon and second vertical separators
are removed. The maximum storage volume for that unit is then 2 x 2 x 1 = 4 cubic meters:

Example 2:
Input:
n = 3 m = 3 h = [2] v = [2]

Output: 4
Explanation:
There are n = m = 3 separators in the vertical and horizontal directions. Separators to remove are
h = [2] and v = [2]. so the unit looks like this:

Return the volume of the biggest space, 4, as the answer.

Example 3:
Input:
n = 3 m = 2 h = [1, 2, 3] v = [1, 2]

Output: 12
Explanation:
Initially there are n = 3 horizontal and m = 2 vertical separators. Remove separators h = [1, 2, 3]
and v = [1,2]. so the unit looks like this:

The volume of the biggest storage space is 12 cubic meters.
'''

def storage_optimization(n: int, m: int, h: [int], v: [int]) -> int:
    h.sort()
    v.sort()
    maxH = 0
    maxV = 0
    prev = 0
    seq = 0

    # try to find the longest consecutive sequence
    # for both h and v separators
    for i in range(len(h)):
        if h[i] - prev == 1:
            seq += 1
        else:
            seq = 1
        maxH = max(seq, maxH)
        prev = h[i]

    seq = 0
    prev = 0
    for i in range(len(v)):
        if v[i] - prev == 1:
            seq += 1
        else:
            seq = 1
        maxV = max(seq, maxV)
        prev = v[i]
    return (maxH + 1) * (maxV+1)