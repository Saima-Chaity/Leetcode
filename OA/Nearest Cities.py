'''Nearest Cities

There are multiple cities within a large geographic region. The cities are arranged on a graph that
has been divided up like an ordinary Cartesian plane. Each city is located at an integral (x, y)
coordinate intersection. City names and locations are given in the form of three arrays: c, x, and y.
Which are aligned by the index to provide the city name (c[i]), and its coordinates, (x[i], y[i]).

Write an algorithm to determine the name of the nearest city that shares either an x or a y coordinate
with the queried city. If no other cities share an x or y coordinate, return NONE. If two cities have
the same distance to the queried city, q[i], consider the one with an alphabetically smaller name
(i.e. 'ab' < 'aba' < 'abb') as the closest choice.

The distance is denoted on a Euclidean plane: the difference in x plus the difference in y.

Input
The input consists of six arguments:

numOfCities: an integer representing the number of cities

cities: a list of strings representing the names of each city [i]

xCoordinates: a list of integers representing the X coordinates of each city[i]

yCoordinates: a list of integers representing the Y-coordinates of each city[i]

numOfQueries: an integer representing the number of queries

queries: a list of strings representing the names of the queried cities

Output
Return a list of strings representing the name of the nearest city that shares either an x or a y
coordinate with the queried city.

Note
Each character of all c[i] and q[i] is in the range ascii [a-z, 0-9,-].

All city name values, c[i], are unique. All cities have unique coordinates.

Constraints
1 <= numOfCities, numOfQueries < 10^5

1 < xCoordinates[i], yCoordinates[i] <= 10^9

1 < length of queries[i] and cities[i] <= 10

Examples
Example 1:
Input:
numOfCities = 3

cities = ["c1", "c2","c3"]

xCoordinates = [3, 2, 1]

yCoordinates = [3, 2, 3]

numOfQueries = 3

queries = ["c1", "c2", "c3"]

Output: ["c3", NONE, "c1"]
Explanation:
There are three points (3,3), (2,2) and (1,3) represent the coordinates of the cities on the graph.
The nearest city to c1 is c3, which shares a y value (distance = (3-1) + (3-3) = 2). City c2 does
not have the nearest city as any share an x or y with c2, so this query returns NONE. A query of c3
returns c1 based on the first calculation. The returned array after all queries are complete
is [c3, NONE, c1].

Example 2:
Input:
numOfCities = 5

cities = ["green", "red","blue", "yellow", "pink"]

xCoordinates = [100, 200, 300, 400, 500]

yCoordinates = [100, 200, 300, 400, 500]

numOfQueries = 5

queries = ["green", "red", "blue", "yellow", "pink"]

Output: [NONE, NONE, NONE, NONE, NONE]
Explanation:
No nearest cities because none share the same x or y.
'''

# Another approach
from collections import defaultdict


def findNearestCities(numOfCities: int, cities: List[str], xCoordinates: List[int], yCoordinates: List[int],
                      numOfQueries: int, queries: List[str]) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE

    class City:
        def __init__(self, name, x, y):
            self.name = name
            self.x = x
            self.y = y

        def dist(self, other_city):
            return (self.x - other_city.x) ** 2 + (self.y - other_city.y) ** 2

    from collections import defaultdict
    xs = defaultdict(list)  # x_coordinate: [city]
    ys = defaultdict(list)
    city_by_name = {}
    for i in range(numOfCities):
        name = cities[i]
        city = City(name, xCoordinates[i], yCoordinates[i])
        xs[city.x].append(city)
        ys[city.y].append(city)
        city_by_name[name] = city
    ans = []
    cache = {}
    for name in queries:
        if name in cache:
            ans.append(cache[name])
            continue
        city = city_by_name[name]
        search_cities = xs[city.x] + ys[city.y]
        if len(
            search_cities) == 2:  # the target city itself is always in xs and ys, so if there are only two elements, no other city is in the list, we add NONE to the final result
            ans.append('NONE')
            continue
        search_cities.sort(key=lambda x: x.dist(city))
        closest = search_cities[2].name
        ans.append(closest)
        cache[city.name] = closest
        cache[closest] = city.name
    return ans



# class City:
#     def __init__(self, name, x, y):
#         self.name = name
#         self.x = x
#         self.y = y
#
#     def dist(self, other_city):
#         return (self.x - other_city.x) ** 2 + (self.y - other_city.y) ** 2

from collections import defaultdict
class Solution:
    def nearestCities(self, numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries):

        def getDistance(qIndex, cityIndex):
            i = pointToIndex[qIndex]
            j = pointToIndex[cityIndex]
            distance = abs(xCoordinates[i] - xCoordinates[j]) + abs(yCoordinates[i] - yCoordinates[j])
            return distance

        xList = defaultdict(list)
        yList = defaultdict(list)
        pointToIndex = {}
        for i in range(numOfCities):
            name = cities[i]
            # city = City(name, xCoordinates[i], yCoordinates[i])
            xList[xCoordinates[i]].append(name)
            yList[yCoordinates[i]].append(name)
            pointToIndex[name] = i

        result = [None] * (len(queries))
        cache = {}
        i = 0
        for query in queries:
            if query in cache:
                result.append(cache[query])
            else:
                queryIndex = pointToIndex[query]
                xCity = xList[xCoordinates[queryIndex]]
                yCity = yList[yCoordinates[queryIndex]]
                if len(xCity) == 1 and len(yCity) == 1:
                    i += 1
                    continue

                minDistance = float('inf')
                closet = None
                for item in xCity:
                    if item == query:
                        continue
                    distance = getDistance(query, item)
                    if distance < minDistance:
                        minDistance = distance
                        closet = item

                for item in yCity:
                    if item == query:
                        continue
                    distance = getDistance(query, item)
                    if distance < minDistance:
                        minDistance = distance
                        closet = item

                result[i] = closet
                cache[query] = closet
                i += 1
        return result



numOfCities = 3
cities = ["c1", "c2","c3", "c4"]
xCoordinates = [3, 2, 1]
yCoordinates = [3, 2, 3]
numOfQueries = 3
queries = ["c1", "c2", "c3"]

#Output: ["c3", NONE, "c1"]
print(Solution.nearestCities((), numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries))

numOfCities = 5
cities = ["green", "red", "blue", "yellow", "pink"]
xCoordinates = [100, 200, 300, 400, 500]
yCoordinates = [100, 200, 300, 400, 500]
numOfQueries = 5
queries = ["green", "red", "blue", "yellow", "pink"]

# Output: [NONE, NONE, NONE, NONE, NONE]
print(Solution.nearestCities((),numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries))

numOfCities = 6
cities = ["green", "yellow", "red", "blue", "grey", "pink"]
xCoordinates = [10, 20, 15, 30, 10, 15]
yCoordinates = [30, 25, 30, 40, 25, 25]
numOfQueries = 4
queries = ["grey", "blue", "red", "pink"]

# Output: [NONE, NONE, NONE, NONE, NONE]
print(Solution.nearestCities((),numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries))