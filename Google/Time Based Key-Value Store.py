'''Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

Design a time-based key-value data structure that can store multiple values for the same key at
different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with
timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the
largest timestamp_prev. If there are no values, it returns "".

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3
and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "ba2r" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
'''

from collections import OrderedDict
class TimeMap:

    def __init__(self):
        self.time_mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_mapping:
            self.time_mapping[key] = OrderedDict()
        self.time_mapping[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_mapping:
            dictValues = self.time_mapping[key]
            temp = []
            result = ""
            while dictValues:
                time, value = dictValues.popitem()
                temp.append((time, value))
                if time <= timestamp:
                    result = value
                    break

            while temp:
                time, value = temp.pop()
                self.time_mapping[key][time] = value
            return result
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# Using Binary Search
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_mapping[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_mapping:
            return ""

        dictValues = self.time_mapping[key]
        left = 0
        right = len(dictValues) - 1
        while left < right:
            mid = left + (right - left) // 2
            if dictValues[mid][1] < timestamp:
                left = mid + 1
            elif dictValues[mid][1] > timestamp:
                right = mid - 1
            else:
                return dictValues[mid][0]

        if dictValues[right][1] <= timestamp:
            return dictValues[right][0]
        return "" if right < 0 else dictValues[right - 1][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)