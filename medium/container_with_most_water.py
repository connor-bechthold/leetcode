class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = len(height) - 1
        left = 0 
        right = width
        largest = 0
        while width:
            area = min(height[left], height[right]) * width
            largest = max(largest, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            width -= 1
        return largest
