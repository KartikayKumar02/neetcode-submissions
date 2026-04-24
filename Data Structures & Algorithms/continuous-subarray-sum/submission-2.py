class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        sums = 0
        hashmap[0] = -1
        for i in range(len(nums)):
            sums += nums[i]
            if sums % k not in hashmap:
                hashmap[sums % k] = i
            else:
                if i - hashmap[sums % k] >= 2:
                    return True
        print(hashmap.keys())
        return False
        