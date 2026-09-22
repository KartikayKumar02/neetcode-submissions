"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        sorted_intervals = sorted(intervals, key = lambda x:x.start)

        minheap = []

        for interval in sorted_intervals:
            start, end = interval.start, interval.end
            if len(minheap) !=0 and minheap[0] <= start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, end)
        return len(minheap)