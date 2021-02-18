'''Min Heap in Python
'''

class MinHeap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0

    def swap(self, parent, child):
        self.heap_list[parent], self.heap_list[child] = self.heap_list[child], self.heap_list[parent]

    def shiftUp(self, i):
        # While the element is not the root or the left element
        while i // 2 > 0:
            if self.heap_list[i//2] > self.heap_list[i]:
                self.swap(i//2, i)
            i = i // 2

    def sift_down(self, i):
        # if the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            min_child_index = self.min_child(i)
            # Swap the values of the current element is greater than its min child
            if self.heap_list[i] > self.heap_list[min_child_index]:
                self.swap(i, min_child_index)
            i = min_child_index

    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            # return min child
            if self.heap_list[i * 2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1

    def insert(self, k):
        """
        Inserts a value into the heap
        """
        self.heap_list.append(k)
        self.current_size += 1
        self.shiftUp(self.current_size)

    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return 'Empty'
        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.sift_down(1) # Move down the root (value at index 1) to keep the heap property
        return root

"""
Driver program
"""
# Same tree as above example.
my_heap = MinHeap()
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)
my_heap.insert(5)
my_heap.insert(60)
my_heap.insert(7)
my_heap.insert(-5)
my_heap.insert(6)
my_heap.insert(-7)

for i in range(10):
    print(my_heap.delete_min())  # removing min node i.e 5