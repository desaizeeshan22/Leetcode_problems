from heapq import heappop,heappush
def maxEvents(events):
    events.sort()
    total_days = max(end for start, end in events)
    day = 0
    event_id = 0
    num_events_attended = 0
    min_heap = []

    for day in range(1, total_days + 1):
        # Add all the events that start today
        while event_id < len(events) and events[event_id][0] == day:
            heappush(min_heap, events[event_id][1])
            event_id += 1

        # Remove all the events whose end date was before today
        while min_heap and min_heap[0] < day:
            heappop(min_heap)

        # if any event that can be attended today, let's attend it

        if min_heap:
            heappop(min_heap)
            num_events_attended += 1

    return num_events_attended

print(maxEvents([[1,4],[1,1],[3,4],[2,2],[4,4]]))