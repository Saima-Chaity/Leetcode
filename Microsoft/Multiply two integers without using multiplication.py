'''Multiply two integers without using multiplication'''

'''Time Complexity: O(y) where y is the second argument to function multiply().'''

def multiply(x, y):
    if y == 0:
        return 0
    if y > 0:
        return x + multiply(x, y-1)
    if y < 0:
        return - multiply(x, -y)

print(multiply(5, 2))
print(multiply(5, -11))