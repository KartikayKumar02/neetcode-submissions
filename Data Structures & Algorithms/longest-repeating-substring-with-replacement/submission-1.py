class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right =0,0

        maxlen = 0
        max_freq_element = 0
        freq = defaultdict(int)
        while right < len(s):
            freq[s[right]] += 1
            max_freq_element = max(max_freq_element,freq[s[right]])
            
            while (right - left + 1) - max_freq_element > k:
                freq[s[left]] -= 1
                left += 1
            maxlen = max(maxlen, right - left + 1)
            right += 1
        return maxlen
                
