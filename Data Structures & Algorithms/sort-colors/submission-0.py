class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        #nums = [1,0,1,2]
        # {1: 2 , 0: 1, 2: 1}
        # 1,2 ,3 
        for number in nums:
            count[number] += 1
        
        index = 0

        # since we have 3 numbers :1,2,3
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index +=1
