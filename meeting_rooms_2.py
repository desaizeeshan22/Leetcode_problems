import heapq
#
# Given an array of meeting time intervals intervals
# where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Approach: 1)Earliest meeting to be scheduled first aka sort the meetings on their start time and
# assign a room to the  meeting with the lowest start time
# 2)Use a priority queue (a min heap by default) which stores the meetings with the lowest start times in the
# front of the queue
# 3)From here just check if the start times of the upcoming meetings lie at or after the end times of the first queue
# element if yes free up the room at the start of the queue
# 4) The number of rooms in the priority queue at the end is the minimum number of rooms required to schedule meetings
def meeting_rooms(intervals):
    intervals.sort(lambda x:x[0])## sort meetings by start times aka starti in ascending order
    meeting_rooms=[intervals[0][1]] ## meeting with the earliest start time assigned the first meeting room
    for interval in intervals:
        if interval[0]>=meeting_rooms[0]:## if the new meeting to be added has a start time after the current meeting
            #aka the first in the queue(meeting with the earliest end time) then free up the room by popping it
            heapq.heappop(meeting_rooms)
        ## min heap by default the meetings with the earliest end times added at the front of the queue
        heapq.heappush(meeting_rooms,interval[1])
    return len(meeting_rooms) ## return number of rooms at the end of the interval list