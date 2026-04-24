class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        final = []
        result = []
        freq = {}
        for sublist in grid:
            result.extend(sublist)
        # [1,3,2,2]
        freq = Counter(result)
        # 1: 1 , 2 : 2 , 3: 1
        for key,value in freq.items():
            if value > 1:
                final.append(key)
        actual = []
        for i in range(len(grid) ** 2):
            actual.append(i + 1)
        # [1,2,3,4]
        for i in actual:
            if i not in result:
                final.append(i)
        return final
                 



        