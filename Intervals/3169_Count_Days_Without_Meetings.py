'''
1. The meetings are first sorted so that we can process them in increasing order of start day.

2. We maintain a variable lastMaxDay which tracks the farthest day covered by all processed meetings so far.

3. For each meeting:
   - If the current meeting starts after lastMaxDay + 1,
     then there is a gap between the previous covered range and this meeting.
   - That gap represents free days and is added to freeDay.

4. Whether meetings overlap or not, we always update lastMaxDay = max(lastMaxDay, endDay)
   to merge overlapping intervals.

5. After processing all meetings, any remaining days from lastMaxDay to 'days'
   are also free and added to freeDay.

6. max(0, days - lastMaxDay) ensures we do not subtract into negative values
   when meetings extend beyond the given number of days.
'''
# Step-by-step explanation:
#
# days = 50
#
# Sorted meetings:
# [[4,8], [7,42], [9,18], [9,33], [18,19], [22,31], [23,39], [30,46]]
#
# --------------------------------------------------
# Meeting [4,8]
#
# startDay = 4
# endDay = 8
# lastMaxDay = 0
#
# Check:
# 4 > 0 + 1
# 4 > 1 -> True
#
# This means days 1, 2, and 3 are free.
#
# freeDay = 0 + (4 - 0 - 1)
# freeDay = 3
#
# Update lastMaxDay:
# lastMaxDay = max(0, 8)
# lastMaxDay = 8
#
# --------------------------------------------------
# Meeting [7,42]
#
# startDay = 7
# endDay = 42
# lastMaxDay = 8
#
# Check:
# 7 > 8 + 1
# 7 > 9 -> False
#
# This meeting overlaps with [4,8].
# So no new free days are added.
#
# Update lastMaxDay:
# lastMaxDay = max(8, 42)
# lastMaxDay = 42
#
# --------------------------------------------------
# Meeting [9,18]
#
# startDay = 9
# endDay = 18
# lastMaxDay = 42
#
# Check:
# 9 > 42 + 1
# 9 > 43 -> False
#
# Already fully covered by [7,42].
#
# lastMaxDay = max(42, 18)
# lastMaxDay = 42
#
# --------------------------------------------------
# Meeting [9,33]
#
# Inside [7,42]
#
# lastMaxDay = 42
#
# --------------------------------------------------
# Meeting [18,19]
#
# Inside [7,42]
#
# lastMaxDay = 42
#
# --------------------------------------------------
# Meeting [22,31]
#
# Inside [7,42]
#
# lastMaxDay = 42
#
# --------------------------------------------------
# Meeting [23,39]
#
# Inside [7,42]
#
# lastMaxDay = 42
#
# --------------------------------------------------
# Meeting [30,46]
#
# Extends the range beyond 42
#
# lastMaxDay = max(42, 46)
# lastMaxDay = 46
#
# --------------------------------------------------
# Final values:
#
# freeDay = 3
# lastMaxDay = 46
#
# Remaining free days after last meeting:
#
# freeDay = freeDay + max(0, days - lastMaxDay)
# freeDay = 3 + max(0, 50 - 46)
# freeDay = 3 + 4
# freeDay = 7
#
# --------------------------------------------------
# Final Answer = 7

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        freeDay = 0
        lastMaxDay = 0

        for i in range(len(meetings)):
            startDay = meetings[i][0]
            endDay = meetings[i][1]

            if startDay > lastMaxDay + 1:
                freeDay = freeDay + (startDay - lastMaxDay - 1)

            lastMaxDay = max(lastMaxDay, endDay)

        freeDay = freeDay + max(0, days - lastMaxDay)

        return freeDay
