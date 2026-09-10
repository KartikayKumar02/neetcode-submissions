class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force approach

        maxlen = 1
        maxstr = s[0]
        if not s:
            return 

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                substr = s[i:j+1]
                if substr == substr[::-1]:
                    if len(substr) > maxlen:
                        maxlen = max(maxlen,len(substr))
                        maxstr = substr
        return maxstr
        