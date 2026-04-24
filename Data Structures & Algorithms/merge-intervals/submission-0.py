class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []


        for i in range(len(intervals)):
            if result == [] or intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(intervals[i][1],result[-1][1])
        return result
        