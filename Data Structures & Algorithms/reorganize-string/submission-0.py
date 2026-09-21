class Solution:
    def reorganizeString(self, s: str) -> str:
        # {a:1,x:1,y:2}
        heap = []
        result = ""

        freq = Counter(s)

        for key,value in freq.items():
            heapq.heappush(heap,(-value,key))
         # axyy
         #{a:1, x : 1, y : 2}

        prev = (0,"")

        while heap:
            value, key = heapq.heappop(heap) # y


            result += key # y
            
            if prev[0] < 0:
                heapq.heappush(heap,prev)
            prev = (value + 1,key) # y: 1
        
        return "".join(result) if len(result) == len(s) else ""
            
        