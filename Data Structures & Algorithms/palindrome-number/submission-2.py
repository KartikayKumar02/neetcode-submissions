class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        num = x
        while num > 0:
            last_digit = num % 10
            reverse = reverse * 10 + last_digit
            num = num // 10
        return reverse == x
        