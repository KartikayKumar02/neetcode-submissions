class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right = 0,0

        minlen = float('inf')
        sums = 0
        # [2,1,5,1,5,3]
        while right < len(nums):
            sums += nums[right] # 14

            while sums >= target:
                minlen = min(minlen, right - left + 1)
                sums -= nums[left] # 6
                left += 1 
                 # 
            right += 1
        return minlen if minlen != float('inf') else 0

        