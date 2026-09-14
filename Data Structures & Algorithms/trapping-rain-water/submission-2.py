#  $\min(\text{leftMax}, \text{rightMax}) - \text{height}[i]$.
class Solution:
    def trap(self, height: List[int]) -> int:
        # base case
        if not height:
            return 0
        
        total_water = 0
        left, right = 0, len(height) - 1

        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1 # moving left first because we just had initialized leftmax as = left
                leftMax = max(leftMax,height[left])
                total_water += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                total_water += rightMax - height[right]
        return total_water








        