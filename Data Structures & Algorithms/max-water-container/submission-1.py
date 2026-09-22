class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxarea = 0
        if not heights:
            return 0
        while left < right:
            
            maxarea = max(maxarea, (right - left) * min(heights[left],heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxarea