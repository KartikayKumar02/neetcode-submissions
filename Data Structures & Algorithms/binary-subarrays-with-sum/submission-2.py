from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        current_sum = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        count = 0

        for number in nums:
            current_sum += number # 1, 1,2, 2,3
            if (current_sum - goal) in prefix_sum:
                count += prefix_sum[current_sum - goal] # 3        
            prefix_sum[current_sum] += 1 # 0 : 1, 1: 2,2: 2
        return count