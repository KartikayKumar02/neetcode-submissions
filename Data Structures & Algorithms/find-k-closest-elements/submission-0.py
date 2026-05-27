
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        result = []
        result2 = []

        for i in range(len(arr)):
            heapq.heappush(result, (abs(x - arr[i]),arr[i]))
        print(result)
        while k > 0:
            diff,element = heapq.heappop(result)
            result2.append(element)
            k -= 1
        return sorted(result2)

        

