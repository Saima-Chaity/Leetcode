# Minimum Cost Tree From Leaf Values - https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
'''Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
(Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right
subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each
non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
'''

class Solution:
    '''Steps:
    1. Pick up the leaf node with minimum value.
    2. Combine it with its inorder neighbor which has smaller value between neighbors.
    3. Once we get the new generated non-leaf node, the node with minimum value is useless
    (For the new generated subtree will be represented with the largest leaf node value.)
    4. Repeat it until there is only one node.
    '''
    def mctFromLeafValues(self, arr: List[int]) -> int:
        output = 0
        while len(arr) > 1:
            minIndex = arr.index(min(arr))
            if 0 < minIndex < len(arr) - 1:
                output += min(arr[minIndex-1], arr[minIndex+1]) * arr[minIndex]
            else:
                output += arr[1 if minIndex==0 else minIndex-1] * arr[minIndex]
            arr.pop(minIndex)
        return output