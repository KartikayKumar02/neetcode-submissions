class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = collections.defaultdict(int)
        counts[0] = 1
        prefixSum = 0
        total_subarrays = 0



        for i in nums:
            prefixSum += i
            target = prefixSum - goal
            if target in counts:
                total_subarrays += counts[target]
            counts[prefixSum] += 1
        return total_subarrays

        

            






        