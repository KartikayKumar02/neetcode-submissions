class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount = 0
        maxlen = 0
        left, right = 0,0

        while right < len(nums):
            if nums[right] == 0:
                zeroCount += 1
            
            while left <= right and zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            
            maxlen = max(maxlen, right -left + 1)
            right += 1
        return maxlen



        