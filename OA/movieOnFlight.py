'''Question:
You are on a flight and wanna watch two movies during this flight.
You are given List<Integer> movieDurations which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

Find the pair of movies with the longest total duration and return they indexes. If multiple found, return the pair
with the longest movie.

Example 1:

Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
Output: [0, 6]
Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)
'''

class Solution:
    def movieOnFlight(durations, target):
        expectedTarget = target - 30
        output = []
        maxDuration = -1

        sortedDurations = sorted(((duration, index) for index, duration in enumerate(durations)), reverse=True)

        for left in range(len(sortedDurations)):
            for right in range(len(sortedDurations) - 1, left, -1):
                total = sortedDurations[left][0] + sortedDurations[right][0]
                if total <= expectedTarget:
                    if total > maxDuration:
                        maxDuration = total
                        output = [sortedDurations[left][1], sortedDurations[right][1]]
        return sorted(output)


# Another approach
class Solution:
    def movieOnFlight(self, durations, target):
        expectedTarget = target - 30
        output = []
        maxDuration = -1

        durations.sort()
        i = 0
        j = len(durations) - 1
        while i < j:
            total = durations[i] + durations[j]
            if total <= target:
                if total <= expectedTarget:
                    if total > maxDuration:
                        maxDuration = total
                        output = [i, j]
                i += 1
            else:
                j -= 1
        return sorted(output)


print(Solution.movieOnFlight([90, 85, 75, 60, 120, 150, 125], 250))