class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        for i in range(len(intervals)):
            #no merge needed as the first element of the
            #existing list is greater than the last element of 
            #interval to be added
            if intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        result.append(newInterval)
        return result


