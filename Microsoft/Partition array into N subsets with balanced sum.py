'''Partition array into N subsets with balanced sum

Give you one sorted array, please put them into n buckets, we need to ensure we get n sub array
with approximately equal weights.

Example;
input {1, 2, 3, 4, 5} n = 3
output [[[5],[1,4],[2,3]];
'''

'''Time - O(nlog(k)) for heap
'''
import heapq
def subset(arr, n):

    heap = [(0, i) for i in range(n)]
    result = [[] for _ in range(n)]

    for i in range(len(arr)-1, -1, -1):
        value, index = heapq.heappop(heap)
        result[index].append(arr[i])
        total = value + arr[i]
        heapq.heappush(heap, (total, index))
    return result

ip = [1,2,3,4,5,6,7,8,9,10]
total_subsets = 3
print(subset(ip, total_subsets))
print(subset([1,2,3,4,5], 3))
print(subset([2,9,9,10,10], 2))
print(subset([1,2,2,3,3,5],4))
