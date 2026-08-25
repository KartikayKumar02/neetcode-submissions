class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxlen = 0
        left,right = 0,0

        visited = set()
        # zxyzxyz
        while right < len(s):
            

            while s[right] in visited:
                visited.remove(s[left]) # yz
                left += 1 # 1, 2

            visited.add(s[right]) # yzx
            
            maxlen = max(maxlen, right - left + 1)
            right += 1
        return maxlen