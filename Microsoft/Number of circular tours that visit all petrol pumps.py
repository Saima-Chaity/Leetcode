'''Number of circular tours that visit all petrol pumps

Suppose there is a circular road. There are n petrol pumps on that road. You are given two array, a[] and b[],
and a positive integer c. where a[i] denote the amount of fuel we get on reaching ith petrol pump, b[i] denote
the amount of fuel used to travel from ith petrol pump to (i + 1)th petrol pump and c denotes the capacity of
the tank in the vehicle. The task is to calculate the number of petrol pump from where the vehicle will be able
to complete the circle and come back to starting point.

Input : n = 3, c = 3
a[] = { 3, 1, 2 }
b[] = { 2, 2, 2 }
Output : 2
'''

'''Time - 0(n)'''
class Solution:
    def circularToursCount(n, c, a, b) -> int:

        for i in range(0, n, 1):
            a[i+n] = a[i]
            b[i+n] = b[i]

        current_tank = 0
        startIndex = 0
        for i in range(0, 2*n, 1):
            current_tank += a[i]
            current_tank = min(c, current_tank)
            current_tank -= b[i]

            if current_tank < 0:
                startIndex = i + 1
                current_tank = 0

        if startIndex >= n:
            return 0

        result = 1
        extraFuel = [0] * (startIndex+n+1)
        extraFuel[startIndex+n] = 0
        for i in range(1, n, 1):
            index = startIndex+n-i
            extraFuel[index] = max(0, extraFuel[index+1]+b[index] - min(a[index], c))
            if extraFuel[index] == 0:
                result += 1
        return result


'''Time - 0(n2)'''
class Fuel:
    def __init__(self, gas, cost):
        self.gas = gas
        self.cost = cost


class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:

        arr = []
        for i in range(len(gas)):
            fuel = Fuel(gas[i], cost[i])
            arr.append(fuel)

        n = len(arr)
        start = 0
        if len(gas) == 1:
            current_fuel = arr[start].gas - arr[start].cost
            if current_fuel < 0:
                return -1
            return 0

        count = 0
        for i in range(0, len(arr)):
            start = i
            end = (start + 1) % n
            current_fuel = arr[start].gas - arr[start].cost

            if current_fuel < 0:
                continue

            while start != end:
                current_fuel += arr[end].gas - arr[end].cost
                end = (end + 1) % n

            if start == end and current_fuel >= 0:
                count += 1
        return count


if __name__ == '__main__':
    n = 3
    c = 3
    a = [3, 1, 2, 0, 0, 0]
    b = [2, 2, 2, 0, 0, 0]

    print(Solution.canCompleteCircuit((), a, b))

    n = 5
    c = 3
    a = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    b = [1, 2, 1, 1, 1, 0, 0, 0, 0, 0]

    print(Solution.canCompleteCircuit((), a, b))