class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for index in range(len(nums)):
            hashmap[nums[index]] = index
        
        for i in range(len(nums)):
            if target - nums[i] in hashmap and hashmap[target - nums[i]]!= i:
                print(i)
                return [i,hashmap[target - nums[i]]]
        