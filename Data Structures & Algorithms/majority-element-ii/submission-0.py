class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        freq = collections.Counter(nums)
        n = len(nums)

        for key,value in freq.items():
            if value > n//3:
                result.append(key)
        return result