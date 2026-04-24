class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        left = 0
        right = k
        result = s[left:right]
        count = 0
        if k > len(s):
            return 0
        if len(list(set(result))) == len(result):
            count += 1
        
        while right < len(s):
            left += 1
            right += 1
            result = s[left:right]
            if len(list(set(result))) == k:
                count += 1
            
        return count



            
            

            
                




        