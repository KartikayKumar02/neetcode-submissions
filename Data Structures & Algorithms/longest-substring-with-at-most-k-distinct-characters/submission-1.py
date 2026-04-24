class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right  = 0, 0
        maxlen = 0

        counts = Counter()
        while right < len(s):

            counts[s[right]] += 1

            while left <= right and len(counts) > k:
                
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            maxlen = max(maxlen, right - left + 1)
            right += 1

        return maxlen