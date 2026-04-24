class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left,right = 0,0 

        maxfreqelement = 0
        maxlen = 0

        while right < len(s):
            freq[s[right]] += 1
            maxfreqelement = max(maxfreqelement,freq[s[right]])

            if (right - left + 1) - maxfreqelement > k:
                freq[s[left]] -= 1
                left += 1
            maxlen = max(maxlen, right - left + 1)
            right += 1
        return maxlen

        
        