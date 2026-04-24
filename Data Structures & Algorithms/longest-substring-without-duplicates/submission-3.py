
# zxy z xyz
 # l  r 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxlen = 0
        visited = set()

        while right < len(s):
            
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            maxlen = max(maxlen, right - left + 1)
            right += 1
        return maxlen
        