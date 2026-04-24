class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixsum = defaultdict(int)
        sums  = 0
        prefixsum[0] = 1
        count = 0

        for number in nums:
            sums += number
            if (sums - goal) in prefixsum:
                count += prefixsum[sums-goal]
            prefixsum[sums] += 1
        return count


                


        

            






        