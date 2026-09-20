class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxsum = nums[0]

        for num in nums:
            total += num
            maxsum =max(maxsum,total)
            if total < 0:
                total = 0
        return maxsum