from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        CounterRansom = Counter(ransomNote)
        Countermagazine = Counter(magazine)


        for key,value in CounterRansom.items():
            if key in Countermagazine:
                if Countermagazine[key] < value:
                    return False
            else:
                return False
        return True
