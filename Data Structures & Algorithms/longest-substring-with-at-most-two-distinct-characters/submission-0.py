# ccaabbb
# c: 2, a : 2, b: 1
# c:1, a:2, b: 1
# c:0, a:2, b: 1


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0,0

        maxlen = 0
        freq = defaultdict(int)


        while right < len(s):
            
            freq[s[right]] += 1

            while left <= right and len(freq.keys()) > 2 :
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            maxlen = max(maxlen, right - left + 1)


            right += 1 
        return maxlen



        