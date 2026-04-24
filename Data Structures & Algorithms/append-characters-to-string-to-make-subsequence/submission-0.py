class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # ABCDE -> BCD SUBSTRING, ADE SUBSEQUENCE

        i,j =0,0
        count = 0

        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j


            
            
