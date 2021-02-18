'''Find the number of events that can be arranged without any conflicts.
Events are given in an array of strings with the YYYYMMDD format and are processed in the first-come,
first-served manner.
You can assume that there are even number of strings and every ith (0-indexed) event has its beginnig and end given at
the 2ith and 2i+1th position in the input array.
The event times are considered as [startTime, endTime)

Eg:

["20190101", "20190104", "20190103", "20190106", "20190106", "20190107"] = 2
There are only 2 events out of the 3 that can be arranged. This is because the 2nd event ( "20190103", "20190106")
conflicts with the first event ("20190101", "20190104").

["20190101", "20190104", "20200103", "20200106", "20190106", "20190107"] = 3
All 3 events can be arranged. This is because the 2nd event is of the year 2020 (not 2019) and so does not clash
with any other event.

Edit: We CANNOT sort is what the interviewer told me since it has been explicitly mentioned that the events are handled
in first-come, first-served basis. I myself had this idea of sorting it based on the start time of the events similar
to how we do it in the general interval problems but he said I cannot sort it. Which is why I was confused as to how
this would be solved other than O(n^2) brute force :|
'''

import datetime
def dateTime(dates):

    def formatDate(date):
        year, month, day = "", "", ""
        for i in range(len(date)):
            if i <= 3:
                year += date[i]
            elif i > 3 and i <= 5:
                month += date[i]
            else:
                day += date[i]
        currentDate = datetime.date(int(year), int(month), int(day))
        return currentDate

    def book(duration, startDate, calender):
        for i in range(0, duration):
            newDate = formatDate(startDate) + datetime.timedelta(days=i)
            calender.add(newDate)
        return calender

    def availableDate(duration, startDate, calender):
        for i in range(0, duration):
            newDate = formatDate(startDate) + datetime.timedelta(days=i)
            if newDate in calender:
                return False
        return True

    calender = set()
    count = 0
    for i in range(0, len(dates), 2):
        startDate = int(formatDate(dates[i]).strftime('%Y%m%d'))
        endDate = int(formatDate(dates[i+1]).strftime('%Y%m%d'))
        duration = endDate - startDate
        if availableDate(duration, dates[i], calender):
            book(duration, dates[i], calender)
            count += 1
    return count


print(dateTime(["20190101", "20190104", "20190103", "20190106", "20190106", "20190107"])) # 2
print(dateTime(["20190101", "20190104", "20200103", "20200106", "20190106", "20190107"])) # 3