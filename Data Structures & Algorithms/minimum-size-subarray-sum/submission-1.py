class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right = 0,0
        minlen = float('inf')
        current_sum = 0
        while right < len(nums):
            current_sum += nums[right]

            while current_sum >= target:
                minlen = min(minlen, right - left + 1)
                current_sum -= nums[left]
                left += 1
            
            right += 1
        
        return minlen if minlen != float('inf') else 0