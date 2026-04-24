class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLen = 0
        result = set()  # Use a set to keep track of unique characters in the window

        while right < len(s):
            if s[right] not in result:
                result.add(s[right])
                # Update maxLen based on the current window size
                maxLen = max(maxLen, right - left + 1)
                right += 1
            else:
                # Remove the character at `left` and move `left` rightward
                result.remove(s[left])
                left += 1

        return maxLen
