import heapq
class Solution(object):
    def maxEvents(self, events):
        ## number of events attened
        num_events=0
        ##output array to store end times
        res=[]
        # sorting events by start time
        events.sort(key=lambda x:x[0])
        end_day=max(end for start,end in events)
        ##event number
        event_num=0
        for day in range(1,end_day+1):
            # adding the end times of all events starting on the same start day
            while(event_num<len(events))and(events[event_num][0]==day):
                heapq.heappush(res,events[event_num][1]) #pushing end times to the min heap                                    ## aka the event with the least start time is given priority
                event_num+=1
                      
            #if the end date of the event is in the past aka
            #the end date is before the current start date we remove it
            while res and res[0]<day:
                heapq.heappop(res)
            if res:
                heapq.heappop(res)## attend the event with the shortest end time
                num_events+=1## among the events with the same start time
        return num_events
        
        """
        :type events: List[List[int]]
        :rtype: int
        """
        