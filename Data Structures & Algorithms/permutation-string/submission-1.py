from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        left,right = 0, len(s1) - 1
        window_counter = Counter(s2[:len(s1)])

        while right < len(s2):
            if window_counter == s1_counter:
                return True
            
            window_counter[s2[left]] -= 1
            if window_counter[s2[left]] == 0:
                del window_counter[s2[left]]
            
            right += 1
            left += 1
            if right < len(s2):
                window_counter[s2[right]] += 1
        return False
        