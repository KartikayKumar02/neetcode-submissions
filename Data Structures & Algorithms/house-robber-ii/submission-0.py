class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(houses):
            prev1,prev2 = 0,0

            for house in houses:
                current_max = max(prev1,prev2 + house)
                prev2 = prev1
                prev1 = current_max
            return prev1
        return max(helper(nums[:-1]), helper(nums[1:]))
        
        