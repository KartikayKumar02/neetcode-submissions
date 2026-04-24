class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        reverse = 0
        num = x
        while num > 0: # 125, 12, 1
            last_digit = num % 10 # 5, 2, 1
            reverse = reverse * 10 + last_digit #5, 50 + 2= 52, 520 + 1 = 521
            num = num // 10 # 12.5 -> 12 - > 1 -> 0
        return reverse == x