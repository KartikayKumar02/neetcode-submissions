class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        leftmax = height[0]
        rightmax = height[len(height) - 1]
        total_water = 0

        left,right = 0, len(height) - 1

        while left < right:
            if leftmax < rightmax:
                total_water += leftmax - height[left]
                left += 1
                leftmax = max(leftmax, height[left])
                
            else:
                total_water += rightmax - height[right]
                right -= 1
                rightmax = max(rightmax, height[right])
                
        return total_water