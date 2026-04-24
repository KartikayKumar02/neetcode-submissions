class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0, len(heights) - 1
        water_hold = 0
        while left < right:
            water_hold = max(water_hold,min(heights[right],heights[left]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return water_hold

        