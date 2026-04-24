
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1,x2,y1,y2):
            return (math.sqrt((x1 - x2)**2 + (y1-y2)**2))
        heap = []
        for i,j in (points):
            heapq.heappush(heap,(distance(i,0,j,0),[i,j]))
        return [heapq.heappop(heap)[1] for _ in range(k)]
            

        