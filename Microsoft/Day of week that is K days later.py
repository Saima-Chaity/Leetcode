'''Day of week that is K days later

Given current day as day of the week and an integer K, the task is to find the day of the week after K days.

Example 1:
Input:
day = “Monday”
K = 3
Output: Thursday

Example 2:
Input:
day = “Tuesday”
K = 101
Output: Friday'''

def day_of_week(day: str, k: int) -> str:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index = 0
    for i in range(len(days)):
        if days[i] == day:
            index = i
    return days[(index + k) % 7]