class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        prod = 1
        result = 0
        
        while right < len(nums):
            prod = prod * nums[right]
            while left <= right and prod >= k:
                prod = prod // nums[left]
                left += 1
            result += (right -left + 1)
            right += 1
        return result

            



        