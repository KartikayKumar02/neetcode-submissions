class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        count = 0

        for number in nums:
            curr_sum += number
            if curr_sum - k in prefixSum:
                count += prefixSum[curr_sum - k]
            prefixSum[curr_sum] += 1
        return count
