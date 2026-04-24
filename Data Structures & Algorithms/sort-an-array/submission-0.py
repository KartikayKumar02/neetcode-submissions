
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for i in nums:
            heapq.heappush(heap,i)
        small = []
        result = []
        while heap:
            smallest = heapq.heappop(heap)
            result.append(smallest)
        return result
            
        