'''You've created a new programming language, and now you've decided to add hashmap support to it. 
Actually you are quite disappointed that in common programming languages it's impossible to add a 
number to all hashmap keys, or all its values. So you've decided to take matters into your own hands 
and implement your own hashmap in your new language that has the following operations:

insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.
To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains 
the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.'''

class HashMap:
    def __init__(self):
        self.mapping = {}
        self.keyOffSet = 0
        self.valueOffSet = 0
    
    def put(self, key, value):
        keyWithoutOffset = key - self.keyOffSet
        valueWithoutOffset = value - self.valueOffSet
        self.mapping[keyWithoutOffset] = valueWithoutOffset
        print(self.mapping)
    
    def get(self, key):
        keyWithoutOffset = key - self.keyOffSet
        if keyWithoutOffset in self.mapping:
            return self.mapping[keyWithoutOffset] + self.valueOffSet
        return 0
    
    def remove(self, key):
        keyWithoutOffset = key - self.keyOffSet
        if keyWithoutOffset in self.mapping:
            del self.mapping[keyWithoutOffset]
        return None
    
    def addToKey(self, key):
        self.keyOffSet += key
    
    def addToValue(self, value):
        self.valueOffSet += value


hashMap = HashMap()
def customMap(queryType, query):
    summation = 0
    for i in range(len(queryType)):
        currentType = queryType[i]
        if currentType == 'insert':
            hashMap.put(query[i][0], query[i][1])
        elif currentType == 'get':
            summation += hashMap.get(query[i][0])
        elif currentType == 'addToKey':
            hashMap.addToKey(query[i][0])
        elif currentType == 'addToValue':
            hashMap.addToValue(query[i][0])
    return summation

_queryType = ["insert", "insert", "addToValue", "addToKey", "get"] 
_query = [[1, 2], [2, 3], [2], [1], [3]] 
#the output should be hashMap(queryType, query) = 5.
print(customMap(_queryType, _query))

_queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"] 
_query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]]
#the output should be hashMap(queryType, query) = 6.
print(customMap(_queryType, _query))
