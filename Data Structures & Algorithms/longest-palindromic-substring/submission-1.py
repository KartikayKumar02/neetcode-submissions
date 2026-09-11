class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        max_len = 0
        max_str = s[0]

        for i in range(len(s)):
            # 1. Odd length check (center at i)
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    max_str = s[left : right + 1]
                left -= 1
                right += 1

            # 2. Even length check (center between i and i + 1)
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    max_str = s[left : right + 1]
                left -= 1
                right += 1

        return max_str