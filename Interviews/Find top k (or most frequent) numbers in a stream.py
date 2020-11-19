'''Find top k (or most frequent) numbers in a stream
Given an array of n numbers. Your task is to read numbers from the array and keep at-most K numbers at the
top (According to their decreasing frequency) every time a new number is read. We basically need to print top k
numbers sorted by frequency when input stream has included k distinct elements, else need to print all
distinct elements sorted by frequency.

Examples:

Input : arr[] = {5, 2, 1, 3, 2}
k = 4
Output : 5 2 5 1 2 5 1 2 3 5 2 1 3 5

Input : arr[] = {5, 2, 1, 3, 4}
k = 4
Output : 5 2 5 1 2 5 1 2 3 5 1 2 3 4
'''

def topKNumbers(arr, k):
    top = [0 for i in range(k+1)]
    mapping = {i:0 for i in range(k+1)}
    for index, num in enumerate(arr):
        if num not in mapping:
            mapping[num] = 1
        else:
            mapping[num] += 1

        top[k] = num
        i = top.index(num)
        i -= 1
        while i >= 0:
            if mapping[top[i]] < mapping[top[i+1]]:
                top[i], top[i+1] = top[i+1], top[i]
            elif mapping[top[i]] == mapping[top[i+1]] and top[i] > top[i+1]:
                top[i], top[i+1] = top[i+1], top[i]
            else:
                break
            i -= 1

        i = 0
        while i < k and top[i] != 0:
            print(top[i], end=' ')
            i += 1

topKNumbers([ 5, 2, 1, 3, 2 ], 4)
