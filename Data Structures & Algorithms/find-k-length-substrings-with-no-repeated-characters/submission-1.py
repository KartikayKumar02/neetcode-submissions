class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        right,left = 0,0 
        count = 0

        visit = set()


        while right < len(s):
            while s[right] in visit:
                visit.remove(s[left])
                left += 1
            
            visit.add(s[right])

            if (right - left + 1) > k:
                visit.remove(s[left])
                left += 1
            
            if (right - left + 1) == k:
                count += 1
            
            right += 1

        return count