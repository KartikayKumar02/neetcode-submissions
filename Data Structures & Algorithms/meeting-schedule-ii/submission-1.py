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
        intervals.sort(key=lambda x: x.start)
        min_heap = []
        # 0,40 , 5,10 , 15,20  

        for i in intervals:
            if min_heap and min_heap[0] <= i.start: # 10 <= 20
                heapq.heappop(min_heap) # 40
            heapq.heappush(min_heap, i.end) # 20,40
        return len(min_heap)