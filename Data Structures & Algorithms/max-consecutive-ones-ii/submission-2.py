class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 0
        zeroCount = 0
        maxno = 0
        #  nums = [1,0,1,1,0,1]
        while right < len(nums):
            if nums[right] == 0:
                zeroCount += 1 #1, 2
            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1 # 3
                left += 1 # 1
            maxno = max(maxno,right - left + 1) # 1,2,3,4
            right += 1
        return maxno

        