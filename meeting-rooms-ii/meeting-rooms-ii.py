
class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x[0])
        meeting_rooms=[]
        heapq.heappush( meeting_rooms, intervals[0][1])
        for interval in intervals[1:]:
            if meeting_rooms[0]<=interval[0]:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms,interval[1])
        return len(meeting_rooms)
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        