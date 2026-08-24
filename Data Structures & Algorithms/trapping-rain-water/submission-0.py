class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        leftmax, rightmax = 0,0

        total_water = 0

        while left < right:
            if height[left] < height[right]:
                leftmax = max(leftmax, height[left])
                total_water += leftmax - height[left]
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                total_water += rightmax - height[right]
                right -= 1
        return total_water

        