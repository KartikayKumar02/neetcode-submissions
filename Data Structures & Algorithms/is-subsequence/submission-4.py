
# Input: s = "abc", t = "aabbcc"


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        if s == "":
            return True
        if t == "" and s != "":
            return False
        
        while p2 < len(t) and p1 < len(s):
            if s[p1] == t[p2]:
                
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        
        if p1 == len(s):
            return True
        else:
            return False